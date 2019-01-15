from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class SetDistanceWorkout(FlaskForm):
  
  distance = StringField('distance',
    validators=[Length(min=1, max=5)])
  
  split = StringField('split', 
    validators=[Length(min=1, max=3)])

  submit = SubmitField('Set Workout')

class SetTimeWorkout(FlaskForm):

  hours = StringField('hours',
    validators=[Length(min=0, max=1)])
  
  minutes = StringField('mintues',
    validators=[Length(min=0, max=2)])

  seconds = StringField('seconds',
    validators=[ Length(min=0, max=2)])

  submit = SubmitField('Set Workout')
