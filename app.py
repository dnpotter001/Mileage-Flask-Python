from flask import Flask, render_template, url_for, flash,redirect
from form import SetWorkoutForm
import pyrow
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
    ergs = list(pyrow.find())
    pm5 = pyrow.pyrow(ergs[0])
    pm5.set_workout(distance=form.distance.data)
    return redirect(url_for('erg'))
  return render_template('erg.html', title='Erg Control', form=form)

if __name__ == '__main__':
  app.run(debug=True)

# ergs = list(pyrow.find())
# if len(ergs) == 0:
#     print('No ergs found')

# erg = pyrow.pyrow(ergs[0])
# print "Connected to erg."

# erg.set_workout(distance=2000, split=100, pace=120)
