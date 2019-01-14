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
  ergInfo = 0
else:
  isConnected = True
  for erg in ergs:
    erg = pyrow.pyrow(erg)
  ergInfo = erg.get_erg()

ergConnection = {
  "connected": isConnected,
  "count": len(ergs),
  "ergData": ergInfo
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
    form=form,
    ergConnection=ergConnection
  )

@app.route("/about")
def about():
  return render_template('about.html', title="About")

@app.route('/ergControl', methods=['GET', 'POST'])
def ergControlg():
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
