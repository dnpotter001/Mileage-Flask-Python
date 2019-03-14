import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bson import ObjectId
from mileage import mongo

class GSheet(object):

  def __init__(self, user_id):
    self.sheetsURL = mongo.db.users.find_one({"_id": ObjectId(user_id)},{"_id": 0, "gsheet":1})

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Mileage/Mileage-961a3e01a7a1.json', scope)
    client = gspread.authorize(credentials)
    wks = client.open_by_url('https://docs.google.com/spreadsheets/d/1RIXQXN7zVlO1exgvXSNrhGRMgDqrf2JIFRg_ycXFcv8/edit#gid=0').sheet1
    #self.url = url

  def add_Workout(self, workout):
    return "hi"
