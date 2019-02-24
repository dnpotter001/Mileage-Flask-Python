from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, PasswordField, BooleanField, FieldList, FormField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Length, InputRequired, NumberRange, EqualTo, ValidationError, Email, DataRequired
from mileage import mongo

class RegistrationForm(FlaskForm):
  firstName = StringField('First Name',
    validators=[InputRequired(), Length(min=2, max=30)],
    render_kw={"placeholder": "First Name"})

  lastName = StringField('Last Name',
    validators=[InputRequired(), Length(min=2, max=30)],
    render_kw={"placeholder": "Last Name"})
  
  email = StringField('Email',
    validators=[InputRequired(), Email()],
    render_kw={"placeholder": "Email"})

  password = PasswordField('Password', 
    validators= [InputRequired()],
    render_kw={"placeholder": "Password"})

  confirmPassword = PasswordField('Confirm Password',
    validators=[InputRequired(), EqualTo('password')],
    render_kw={"placeholder": "Confirm Password"})

  submit = SubmitField('Sign Up')

  def validate_email(self, email):
    if (mongo.db.users.find_one({"email": email.data}) != None):
      raise ValidationError('That email is taken. Please choose a different email')

class LoginForm(FlaskForm):
  email = StringField('Email',
    validators=[InputRequired(), Email()],
    render_kw={"placeholder": "Email"})

  password = PasswordField('Password', 
    validators=[InputRequired()],
    render_kw={"placeholder": "Password"})

  remember = BooleanField('Remember Me')
  
  submit = SubmitField('Login')

class CSVUpload(FlaskForm):

  csvField = FileField('Upload a CSV', 
    validators=[FileRequired(), FileAllowed(['csv'], '.csv files only!')])

  title = StringField('Workout Name: ',
    validators=[DataRequired()],
    render_kw={
      "placeholder": "e.g. Sunday Workout", 
      "required": "required",
      "min": "5",
      "max": "40"})

  submitCSV = SubmitField('Submit')

class UploadSingleInterval(FlaskForm):

  title = StringField('Workout Name: ',
    validators=[DataRequired()],
    render_kw={
      "placeholder": "e.g. Sunday Workout", 
      "required": "required",
      "min": "5",
      "max": "40"})

  distance = IntegerField('Distance: ',
    validators=[DataRequired()],
    render_kw={
      "placeholder":"Meters",
      "id":"singleDistance",
      "required": "required",
      "type":"number"})

  time = StringField('Time: ',
    validators=[DataRequired()],
    render_kw={
      "placeholder":"H:MM:SS",
      "id":"singleTime",
      "required":"required",
      "pattern": r"^(?:(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d).)?([0-9]?\d)$",
      "title":"Hours:Minutes:Seconds"})

  upload = SubmitField('Upload')

class UploadIntervalFixed(FlaskForm):

  title = StringField('Workout Name: ',
    validators=[DataRequired()],
    render_kw={
      "placeholder": "e.g. Sunday Workout", 
      "required": "required",
      "min": "5",
      "max": "40"})
   
  count = IntegerField('Interval Count',
  validators=[DataRequired()],
  render_kw={
    "required":"required",
    "min": "0",
    "max": "100",
    "type":"number"})

  rest = IntegerField('Rest Time: ',
  validators=[DataRequired()],
  render_kw={
    "placeholder":"Minutes:Seconds",
    "id":"restInput",
    "required":"required",
    "pattern":"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$",
    "title":"Minutes:Seconds"})

  upload = SubmitField('Upload')

class UploadIntervalsVariable(FlaskForm):

  title = StringField('Workout Name: ',
  validators=[DataRequired()],
  render_kw={
    "placeholder": "e.g. Sunday Workout", 
    "required": "required",
    "min": "5",
    "max": "40"})
   
  count = IntegerField('Interval Count',
  validators=[DataRequired()],
  render_kw={
    "required":"required",
    "min": "0",
    "max": "100",
    "type":"number"})

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
