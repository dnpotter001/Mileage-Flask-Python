from flask import render_template, url_for, flash, redirect, request
from mileage import app
from mileage.forms import SetWorkoutForm
from mileage import pyrow

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

ergs = list(pyrow.find())
if len(ergs) == 0:
  isConnected = False
  ergData = 0 
else:
  isConnected = True
  for erg in ergs:
    erg = pyrow.pyrow(erg)
    ergData = [{'serial': 123},{'serial': 3857345}]
    ergData.append(erg.get_erg())

ergConnection = {
  "connected": isConnected,
  "count": len(ergData),
  "ergData": ergData,
}

@app.route("/")
@app.route("/home")
@app.route("/feed")
@app.route("/index")
def home():
  form = SetWorkoutForm()
  return render_template(
    'index.html', 
    posts=workouts, 
    title="Your Feed", 
    ergConnection=ergConnection
  )

@app.route("/about")
def about():
  return render_template('about.html', title="About")

@app.route('/erg-control', methods=['GET', 'POST'])
def ergControl():
  form = SetWorkoutForm()
  if form.validate_on_submit():
    for erg in ergs:
      pm = pyrow.pyrow(erg)
      pm.set_workout(distance=int(form.distance.data), split=int(form.split.data))
      flash(f'Setting workout for {form.distance.data}', 'success')

  else: 
    flash('Invalid workout', 'warning')
  return render_template('erg.html', title='Erg Control', form=form, ergConnection=ergConnection)

@app.route('/set_workout')
def set_workout():
  ergs = list(pyrow.find())
  if len(ergs) == 0:
    print('No ergs found')
  pm5 = pyrow.pyrow(ergs[0])
  pm5.set_workout(distance=2000, split=120)
  return 'setting workout'
