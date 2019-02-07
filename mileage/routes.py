from flask import render_template, url_for, flash, redirect, request, g, jsonify, request, make_response
from mileage import app
from mileage.forms import SetDistanceWorkout, SetTimeWorkout, StandardWorkouts, UploadSingleInterval, CSVUpload, LoginForm, RegistrationForm
from . import pyrow
from mileage.sijaxHandlers import ErgHandler 
import flask_sijax
import time
import io, csv, os
from io import StringIO
import json
from mileage.rowfis import MaleFIS, FemaleFIS
from flask_pymongo import PyMongo


#print(plot_tipping_problem_newapi.CalcTip(10, 10))
#dunny test data for the feed
workouts = [
  {
    'author':'David Potter',
    'title': 'Sunday workout',
    'date': '11th Jan 2018'
  },
  {
    'author':'Judith Potter',
    'title': 'Saturday workout',
    'date': '12th Jan 2019'
  },
  {
    'author':'Eve Megaw',
    'title': 'Thursday workout',
    'date': '14th Aug 2019'
  }
]
mongoDB = PyMongo(app)

@app.route("/mongo")
def mongo():
  users = mongoDB.db.users
  users.insert({"name": "David Potter"})

  return "Added user"

@app.route("/")
def welcome():

  return render_template(
    'welcome.html',
    title="Welcome",

  )

@app.route("/login", methods=['GET', 'POST'])
def login():

  login = LoginForm()

  if login.submit.data and login.validate():
      if login.email.data == 'dave@mileage.com' and login.password.data == 'password':
          flash('You have been logged in!', 'success')
          return redirect(url_for('feed'))
      else:
          flash('Login Unsuccessful. Please check username and password', 'danger')

  return render_template(
    'login.html',
    login=login
  )

@app.route("/register", methods=['GET', 'POST'])
def register():

  register= RegistrationForm()

  if register.submit.data and register.validate():
    flash('You have been registered please log in', 'success')
    return redirect(url_for('login'))

  return render_template(
    'register.html',
    register=register
  )

@app.route("/feed")
def feed():

  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()

  return render_template(
    'index.html', 
    posts=workouts, 
    title="Your Feed"
  )

@app.route("/upload", methods=['GET', 'POST'])
def upload():
  singleInterval= UploadSingleInterval()
  csv = CSVUpload()
    

  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()

  return render_template(
    'upload.html', 
    title="Upload a workout",
    singleInterval=singleInterval,
    csv=csv
  )

@app.route("/workout-review", methods=['GET', 'POST'])
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
      flash(f'{upload.filename} successfully uploaded', 'success')

    stream = io.StringIO(upload.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    csvArray = []
    for row in csv_input:
      csvArray.append(row)


    intervalCount = csvArray[15][0]
    intervals = []
    for x in range(0, int(intervalCount)):
      intervals.append(csvArray[x + 22])
  
    workout = { 
      'ty pe': csvArray[4][1],
      'details': csvArray[2][1],
      'intervalCount': intervalCount,
      'units':csvArray[14],
      'overviewLabels':csvArray[13],
      'overview':csvArray[15],
      'intervalLabels':csvArray[20],
      'intervals':intervals
    }
    if (csvArray[15][14] != None):
      catch = -int(csvArray[15][14])
      finish = int(csvArray[15][16])
      slip = int(csvArray[15][15])
      wash = int(csvArray[15][17])
      length = (catch - slip) + (finish - wash)

      print(catch,finish,slip,wash,length)

      maleFIS = MaleFIS()
      maleFisQuality = maleFIS.EvalStroke(catch, finish, slip, wash, length)
      femaleFIS = FemaleFIS()
      femaleFISQuality = femaleFIS.EvalStroke(catch, finish, slip, wash, length)
    else:
      maleFisQuality = "FIS score not available"
      femaleFISQuality = "FIS score not available"

  if g.sijax.is_sijax_request:
    g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
    return g.sijax.process_request()

  return render_template(
    'workout-review.html', 
    title='Erg Control',
    workout=workout,
    zip=zip,
    intervals = workout['intervals'],
    manFis=maleFisQuality,
    womanFis=femaleFISQuality,
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


@app.route("/about")
def about():
  return render_template('about.html', title="About")
