from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, PasswordField, BooleanField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Length, DataRequired, NumberRange, EqualTo, ValidationError, Email

class RegistrationForm(FlaskForm):
  username = StringField('UserName',
    validators=[DataRequired(), Length(min=2, max=30)])
  
  email = StringField('Email',
    validators=[DataRequired(), Email()])

  password = PasswordField('Password', 
    validators= [DataRequired()])

  confirmPassword = PasswordField('Confirm Password',
    validators=[DataRequired(), EqualTo('password')])

  submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
  email = StringField('Email',
    validators=[DataRequired(), Email()])

  password = PasswordField('Password', 
    validators= [DataRequired()])

  remember = BooleanField('Remember Me')

  submit = SubmitField('Login')

class CSVUpload(FlaskForm):

  csvField = FileField('Upload a CSV', 
    validators=[FileRequired(), FileAllowed(['csv'], '.csv files only!')])
  
  submitCSV = SubmitField('Submit')

class UploadSingleInterval(FlaskForm):

  title = StringField('Give your workout a name:',
    validators=[Length(min=5, max=40)],
    render_kw={"placeholder": "e.g. Sunday Workout"})

  distance = IntegerField('Distance',
    validators=([DataRequired(message="This field is required.")]),
    render_kw={"placeholder":"Meters",
               "id":"uploadDistance"})
  
  hours = IntegerField('Time',
  validators=([DataRequired(message="This field is required.")]),
  render_kw={"placeholder":"Hours",
              "id":"uploadHours"})

  minutes = IntegerField('Time',
    validators=([DataRequired(message="This field is required."), NumberRange(min=0, max=59, message='Value Must be between 0 and 59')]),
    render_kw={"placeholder":"Minutes",
               "id":"uploadMinutes"})

  seconds = IntegerField('seconds',
    validators=([DataRequired(message="This field is required."), NumberRange(min=0, max=59, message='Value Must be between 0 and 59')]),
    render_kw={"placeholder":"Seconds",
               "id":"uploadSeconds"})


  upload = SubmitField('Upload')


class SetDistanceWorkout(FlaskForm):
  
  distance = IntegerField('Distance',
    validators=[NumberRange(min=100, max=50000)],
    render_kw={"placeholder": "Distance"})
  
  split = IntegerField('Split',
    validators=[NumberRange(min=100, max=50000)],
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
