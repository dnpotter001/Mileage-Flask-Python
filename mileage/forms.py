from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired, NumberRange

class SetDistanceWorkout(FlaskForm):
  
  distance = StringField('distance',
    validators=[Length(min=1, max=5)])
  
  split = StringField('split', 
    validators=[Length(min=0, max=3)])

  submit = SubmitField('Set Workout')

class SetTimeWorkout(FlaskForm):

  hours = IntegerField('hours',
    validators=[NumberRange(min=0, max=9)])
  
  minutes = IntegerField('mintues',
    validators=[NumberRange(min=0, max=59)])

  seconds = IntegerField('seconds',
    validators=[NumberRange(min=0, max=59)])


  submit = SubmitField('Set Workout')
