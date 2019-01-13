from flask import render_template, url_for, flash, redirect, request
from mileage import app
from mileage.forms import SetWorkoutForm
from mileage import pyrow

workouts = [
  {
    'author':'David Potter',
    'title': 'Sunday workout',
    'date': '11th Jan 2029'
  },
  {
    'author':'Judith Potter',
    'title': 'Saturday workout',
    'date': '12th Jan 2029'
  }
]

@app.route("/")
@app.route("/home")
@app.route("/feed")
@app.route("/index")
def home():
  return render_template('index.html', posts=workouts, title="Your Feed")

@app.route("/about")
def about():
  return render_template('about.html', title="About")

@app.route('/erg', methods=['GET', 'POST'])
def erg():
  form = SetWorkoutForm()
  if form.validate_on_submit():
    return redirect(url_for('set_workout'))
  return render_template('erg.html', title='Erg Control', form=form)

@app.route('/set_workout')
def set_workout():
  ergs = list(pyrow.find())
  if len(ergs) == 0:
    print('No ergs found')
  pm5 = pyrow.pyrow(ergs[0])
  pm5.set_workout(distance=2000, split=120)
  return 'setting workout'
