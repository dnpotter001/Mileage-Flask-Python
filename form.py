from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired

class SetWorkoutForm(FlaskForm):
  
  distance = IntegerField('distance',
    validators=[Length(min=1, max=5)])

  hours = IntegerField('hours',
    validators=[Length(min=0, max=1)])
  
  minutes = IntegerField('mintues',
    validators=[Length(min=0, max=2)])

  seconds = IntegerField('seconds',
    validators=[ Length(min=0, max=2)])
  
  split = IntegerField('split', 
    validators=[Length(min=1, max=3)])

  submit = SubmitField('Set Workout')