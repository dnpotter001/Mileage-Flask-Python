from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired

class SetWorkoutForm(FlaskForm):
  
  distance = IntegerField('distance',
    validators=[DataRequired(), Length(min=1, max=5)])

  hours = IntegerField('hours',
    validators=[DataRequired(), Length(min=0, max=1)])
  
  minutes = IntegerField('mintues',
    validators=[DataRequired(), Length(min=0, max=2)])

  minutes = IntegerField('second',
    validators=[DataRequired(), Length(min=0, max=2)])
  
  split = IntegerField('distance', 
    validators=[DataRequired(), Length(min=1, max=3)])

  submit = SubmitField('Set Workout')