import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bson import ObjectId
from mileage import mongo
from flask import flash

class GSheet(object):

  def __init__(self, user_id):
    sheetsURL = mongo.db.users.find_one(
      {"_id": ObjectId(user_id)},
      {"_id": 0, "gsheet":1}
    )

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Mileage/Mileage-961a3e01a7a1.json', scope)
    client = gspread.authorize(credentials)
    self.sheet = client.open_by_url(sheetsURL['gsheet']).sheet1
    

  def add_Workout(self, workout):
    intervals = []
    for interval in workout.intervals:

      intervals.append(interval['distance'])
      intervals.append(interval['time'])
      intervals.append(interval['rest'])

    #print(intervals)

    self.sheet.append_row([
      workout.title,
      workout.workoutType,
      workout.dateTime,
      *intervals])
    return flash("Added to your google sheet", "success")
    
    


# gsheet = GSheet("5c7e9921c72cf70f380cd763")

# workout = Workout("new workout", "single")
# workout.add_Interval("6000","24:00.0", "0")
# workout.add_Interval("6000","23:00.0", "0")

# gsheet.add_Workout(workout)

