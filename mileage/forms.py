from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import Length, DataRequired, NumberRange

class SetDistanceWorkout(FlaskForm):
  
  distance = StringField('distance',
    validators=[Length(min=1, max=5)])
  
  split = StringField('split', 
    validators=[Length(min=0, max=3)])

  submitDis = SubmitField('Set Workout')

class SetTimeWorkout(FlaskForm):

  hours = IntegerField('hours',
    validators=[NumberRange(min=0, max=9)])
  
  minutes = IntegerField('mintues',
    validators=[NumberRange(min=0, max=59)])

  seconds = IntegerField('seconds',
    validators=[NumberRange(min=0, max=59)])


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
