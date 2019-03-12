from flask import render_template, url_for, flash, redirect, request, g, jsonify, request, make_response
from flask_login import login_user, logout_user, current_user, login_required
from flask_pymongo import PyMongo
import flask_sijax

from bson import Binary, Code, json_util, ObjectId

from mileage import app, bcrypt, mongo, login_manager
from mileage.forms import (SetDistanceWorkout, SetTimeWorkout, StandardWorkouts, 
                           UploadSingleInterval, CSVUpload, LoginForm, RegistrationForm, 
                           UploadIntervalFixed, UploadIntervalsVariable, UpdateAccount)
from mileage.sijaxHandlers import ErgHandler 
from mileage.rowfis import MaleFIS, FemaleFIS
from . import pyrow
from mileage.user import User
from mileage.workout import Workout

import io, csv, os, json, time
from io import StringIO

users = mongo.db.users

@login_manager.user_loader
def load_user(user_id):
    user = users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return None
    return User(str(user['_id']))

@app.route("/")
def welcome():

  return render_template(
    'index.html',
    title="Welcome",

  )

@app.route("/register", methods=['GET', 'POST'])
def register():

  register= RegistrationForm()

  if current_user.is_authenticated:
    return redirect(url_for('feed'))

  if register.submit.data and register.validate():
    hashedPW = bcrypt.generate_password_hash(register.password.data).decode('utf-8')
    users.insert({
      "email": register.email.data,
      "firstName": register.firstName.data,
      "lastName": register.lastName.data,
      "password": hashedPW
    })
    flash(f'Account created for {register.email.data}, your are now able to log in!', 'success')
    return redirect(url_for('login'))
    

  return render_template(
    'register.html',
    register=register
  )

@app.route("/login", methods=['GET', 'POST'])
def login():

  login = LoginForm()
  
  if current_user.is_authenticated:
    return redirect(url_for('feed'))

  if login.submit.data and login.validate():
      user = users.find_one({"email": login.email.data})
      if user and User.validate_login(user['password'], login.password.data):
        user_obj = User(str(user['_id']))
        login_user(user_obj, remember=login.remember.data)
        flash(f'Login Successful, welcome {user["firstName"]}', 'success')
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('feed'))
      else:
        flash('Login Unsuccessful. Please check email and password', 'warning')

  return render_template(
    'login.html',
    login=login
  )

@app.route('/logout')
def logout():
  logout_user()
  flash('Successfully logged out.','success')
  return redirect(url_for('welcome'))

@app.route("/feed")
@login_required
def feed():
  
  pipeline = [
      {"$unwind": {"path": "$workouts"}},
      {"$project": {
          "_id": "$workouts._id",
          "firstName": 1,
          "lastName": 1,
          "title": "$workouts.title",
          "workoutType": "$workouts.workoutType",
          "intervals": "$workouts.intervals",
          "csv": "$workouts.csv",
          "dateTime": "$workouts.dateTime",
          "unixTime": "$workouts.unixtime",
          "maleFis": "$workouts.maleFis",
          "femaleFis": "$workouts.femaleFis"
          }},
      {"$sort": {"unixTime":-1}},
      {"$limit": 20}
  ]
  workouts = users.aggregate(pipeline)

  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()

  return render_template(
    'feed.html', 
     workouts=workouts, 
    title="Your Feed"
  )

@app.route('/profile')
@login_required
def profile():

  pipeline = [
      {"$match": {'_id': ObjectId(current_user._id)}},
      {"$unwind": {"path": "$workouts"}},
      {"$project": {
          "_id": "$workouts._id",
          "firstName": 1,
          "lastName": 1,
          "title": "$workouts.title",
          "workoutType": "$workouts.workoutType",
          "intervals": "$workouts.intervals",
          "csv": "$workouts.csv",
          "dateTime": "$workouts.dateTime",
          "unixTime": "$workouts.unixtime",
          "maleFis": "$workouts.maleFis",
          "femaleFis": "$workouts.femaleFis"
          }},
      {"$sort": {"unixTime":-1}},
      {"$limit": 20}
  ]
  workouts = users.aggregate(pipeline)

  user = users.find_one(
    {"_id": ObjectId(current_user._id)},
    {
      "firstName": 1,
      "lastName": 1,
      "profilePic": 1,
    })


  pp = "static/img/defaultpp.png"
    
  return render_template(
    'profile.html',
    zip=zip,
    workouts=workouts,
    title='Your Profile',
    user=user,
    pp=pp
  )

@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():

  singleInterval= UploadSingleInterval()
  csv = CSVUpload()
  fixedInterval = UploadIntervalFixed()
  variableInterval = UploadIntervalsVariable()

  if singleInterval.upload.data and singleInterval.validate():
    workout = Workout(title= singleInterval.title.data, workoutType="SINGLE")

    timeArray = singleInterval.time.data.split(':')

    if len(timeArray) == 1:
      totalTime = float(timeArray[0])
    if len(timeArray) == 2:
      totalTime = int(timeArray[0]) * 60 + float(timeArray[1])
    if len(timeArray) == 3:
      totalTime = int(timeArray[0]) * 60 * 60 + int(timeArray[1]) * 60 + float(timeArray[2])

    workout.add_Interval(singleInterval.distance.data, totalTime, None)
    
    try:
      users.update_one(
        {'_id': ObjectId(current_user._id)},
        {'$addToSet': {'workouts':workout.__dict__}}
      )
    except:
      flash('Workout correct but error uploading', 'warning')
      return redirect(url_for("upload"))

    flash('Workout Uploaded', 'success')
    return redirect(url_for("feed"))
  
  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()


  return render_template(
    'upload.html', 
    title="Upload a workout",
    singleInterval=singleInterval,
    csv=csv,
    fixedInterval=fixedInterval,
    variableInterval=variableInterval
  )


@app.route("/upload/fixed", methods=['GET','POST'])
@login_required
def uploadFixed():

  if request.method == 'POST' and request.form:
    form = request.form
  else:
    flash('Invalid Upload', 'warning')
    return redirect(url_for('upload'))
  
  workout = Workout(form['title'], "FIXED")

  if not form['count'] or form['count'] == "0":
    flash("You didn't add any intervals", 'warning')
    return redirect(url_for('upload'))

  try:
    restArray = form['rest'].split(':')
    rest = (int(restArray[0]) * 60) + int(restArray[1])
  except:
    flash('Rest in the wrong format, try Minutes:Seconds.', 'warning')
    return redirect(url_for("upload"))

  for x in range(1, int(form['count'])+1):
    try:
      timeArray = form['time' + str(x)].split(':')
      time = (int(timeArray[0]) * 60) + float(timeArray[1])
      workout.add_Interval(form['distance'+ str(x)], time, rest)
    except:
      flash('Time in the wrong format, try Minutes:Seconds.', 'warning')
      return redirect(url_for("upload"))

  try:
    users.update_one(
      {'_id': ObjectId(current_user._id)},
      {'$addToSet': {'workouts':workout.__dict__}}
    )
  except:
    flash('Workout correct but error uploading.', 'warning')
    return redirect(url_for("upload"))

  flash('Workout uploaded', 'success')
  return redirect(url_for("feed"))

@app.route("/upload/variable", methods=['GET','POST'])
@login_required
def uploadVariable():

  if request.method == 'POST' and request.form:
    form = request.form
  else:
    flash('Invalid Upload', 'warning')
    return redirect(url_for('upload'))
  
  workout = Workout(form['title'], "VARIABLE")

  if not form['count'] or form['count'] == "0":
    flash("You didn't add any intervals", 'warning')
    return redirect(url_for('upload'))

  for x in range(1, int(form['count'])+1):
    try:
      restArray = form['rest' + str(x)].split(':')
      rest = (int(restArray[0]) * 60) + int(restArray[1])
      timeArray = form['time' + str(x)].split(':')
      time = (int(timeArray[0]) * 60) + float(timeArray[1])
      workout.add_Interval(form['distance'+ str(x)], time, rest)
    except:
      flash('Time or rest in the wrong format, try Minutes:Seconds.', 'warning')
      return redirect(url_for("upload"))

  try:
    users.update_one(
      {'_id': ObjectId(current_user._id)},
      {'$addToSet': {'workouts':workout.__dict__}}
    )
  except:
    flash('Workout correct but error uploading.', 'warning')
    return redirect(url_for("upload"))

  flash('Workout uploaded', 'success')
  return redirect(url_for("feed"))


@app.route("/workout-review", methods=['GET', 'POST'])
@login_required
def workoutReview():

  if request.method == 'POST': 

    upload = request.files['csvField']
    if not upload:
      flash(f'No file present, please retry', 'warning')
      return redirect(url_for('upload'))

    splitName = upload.filename.split('.')
    fileExt = splitName[1]
    if fileExt != 'csv':
      flash(f'{upload.filename} is not a .csv', 'warning')
      return redirect(url_for('upload'))
    else:
      flash(f"{upload.filename} successfully uploaded as {request.form['title']}", 'success')

    stream = io.StringIO(upload.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    csvArray = []
    for row in csv_input:
      csvArray.append(row)

    workout = Workout(request.form['title'], 'CSV')
    workout.add_csv(csvArray)
    workout.addRowFis()
    fisScores = workout.rowFis()

    try:
        users.update_one(
          {'_id': ObjectId(current_user._id)},
          {'$addToSet': {'workouts':workout.__dict__}}
        )
    except:
        return flash('Workout correct but error uploading, all information is temporary', 'warning')
    
  else: 
    flash('No .CSV uploaded.', 'warning')
    return redirect(url_for('upload'))

  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()

  return render_template(
    'workout-review.html', 
    title='Erg Control',
    workout=workout.csv,
    workoutTitle=workout.title,
    zip=zip,
    intervals = workout.csv['intervals'],
    manFis=fisScores['male'],
    womanFis=fisScores['female'],
    malePlot='/static/img/maleFis.png',
    femalePlot='/static/img/femaleFis.png'
    )
    
@app.route('/erg-control', methods=['GET', 'POST'])
def ergControl():
  
  formDis = SetDistanceWorkout()
  formTime = SetTimeWorkout()
  formSL = StandardWorkouts()

  ergs = list(pyrow.find())

  if formDis.submitDis.data and formDis.validate():
    for erg in ergs:
      pm = pyrow.pyrow(erg)
      try:
        pm.set_workout(distance=formDis.distance.data, split=formDis.split.data)
        flash(f'Setting workout for {formDis.distance.data}m', 'success')

      except ValueError:
        flash(f'Minimum of 1 split and maximum of 50, you entered: {int(formDis.distance.data / formDis.split.data)}', 'warning')

  if formTime.submitTime.data and formTime.validate():
    for erg in ergs:
      pm = pyrow.pyrow(erg)
      pm.set_workout(workout_time=[formTime.hours.data, formTime.minutes.data, formTime.seconds.data])
      flash(f'Setting workout for {formTime.hours.data}:{formTime.minutes.data}:{formTime.seconds.data}', 'success')

  if formSL.submitSL.data and formSL.validate():
    for erg in ergs:
      pm = pyrow.pyrow(erg)
      pm.set_workout(program=int(formSL.standard.data))
      flash(f'Setting workout {formSL.standard.data} on the standard list', 'success')
 
  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()
    
  return render_template(
    'erg.html', 
    title='Erg Control', 
    formDis=formDis, 
    formTime=formTime,
    formSL=formSL
  )

@app.route("/settings",  methods=['GET', 'POST'])
def settings():

  update = UpdateAccount()
  user = users.find_one(
    {"_id": ObjectId(current_user._id)},
    {
      "firstName": 1,
      "lastName": 1,
      "email": 1,
      "bio": 1,
      "club": 1,
      "gsheet": 1
    })

  if update.submit.data and update.validate():
    users.update({"_id": ObjectId(current_user._id)},{
      "firstName":update.firstName.data,
      "lastName":update.lastName.data,
      "email":update.email.data,
      "bio": update.bio.data,
      "club": update.club.data,
      "gsheet": update.gsheet.data,
    })  
    flash("Your profile has been successfully updated.", "success")
    return redirect(url_for("profile"))

  elif request.method == 'GET':
    update.firstName.data = user['firstName']
    update.lastName.data = user['lastName']
    update.email.data = user['email']
    try:
      update.bio.data = user['bio']
      update.club.data = user['club']
      update.gsheet.data = user ['gsheet']
    except KeyError:
      update.bio.data = ''
      update.club.data = ''
      update.gsheet.data = ''

    

  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()

  return render_template(
    'settings.html', 
    title="Settings",
    form=update,
    user=user
    )

@app.route("/about")
def about():

  return render_template('about.html', title="About")
