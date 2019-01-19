from flask import render_template, url_for, flash, redirect, request, g, jsonify
from mileage import app
from mileage.forms import SetDistanceWorkout, SetTimeWorkout, StandardWorkouts
from mileage import pyrow
from mileage.sijaxHandlers import ErgHandler 
import flask_sijax
import time


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

@app.route("/", methods=['GET', 'POST'])
@app.route("/feed")

def home():

  if g.sijax.is_sijax_request:
      g.sijax.register_callback('checkForErgs', ErgHandler.checkForErgs)
      return g.sijax.process_request()
    
  return render_template(
    'index.html', 
    posts=workouts, 
    title="Your Feed"
  )

@app.route("/about")
def about():
  return render_template('about.html', title="About")


@app.route('/erg-control', methods=['GET', 'POST'])
def ergControl():
  formDis = SetDistanceWorkout()
  formTime = SetTimeWorkout()
  formSL = StandardWorkouts()

  if formDis.submitDis.data and formDis.validate():
    for erg in ergs:
      pm = pyrow.pyrow(erg)
      pm.set_workout(distance=int(formDis.distance.data), split=int(formDis.split.data))
      flash(f'Setting workout for {formDis.distance.data}m', 'success')

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


  return render_template(
    'erg.html', 
    title='Erg Control', 
    formDis=formDis, 
    formTime=formTime,
    formSL=formSL,
    ergConnection=ergConnection
  )


