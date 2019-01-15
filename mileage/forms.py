from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import Length, DataRequired, NumberRange

class SetDistanceWorkout(FlaskForm):
  
  distance = StringField('Distance',
    validators=[Length(min=1, max=5)],
    render_kw={"placeholder": "Distance"})
  
  split = StringField('Split', 
    validators=[Length(min=0, max=3)],
    render_kw={"placeholder": "Split"})

  submitDis = SubmitField('Set Workout')

class SetTimeWorkout(FlaskForm):

  hours = IntegerField('Hours',
    validators=[NumberRange(min=0, max=9)],
    render_kw={"placeholder": "Hours"})
  
  minutes = IntegerField('Mintues',
    validators=[NumberRange(min=0, max=59)],
    render_kw={"placeholder": "Minutes"})

  seconds = IntegerField('Seconds',
    validators=[NumberRange(min=0, max=59)],
    render_kw={"placeholder": "Seconds"})


  submitTime = SubmitField('Set Workout')

class StandardWorkouts(FlaskForm):

  standard = SelectField('Standard List', 
    choices=[
      ('1', '2000m'), 
      ('2', '5000m'),
      ('3', '10000m'),
      ('4', '30:00'),
      ('5', '500m/1:00r')])

  submitSL = SubmitField('Set Workout')
