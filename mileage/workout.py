import datetime
import time
from bson import ObjectId
from mileage.rowfis import MaleFIS, FemaleFIS
from mileage.gsheet import GSheet
from flask_login import current_user

class Workout(object):

  def __init__(self, title, workoutType):
    self._id = ObjectId()
    self.title = title
    self.workoutType = workoutType
    self.intervals = []
    self.dateTime = datetime.datetime.today().strftime('%d-%m-%Y')
    self.unixtime = int(time.time())

  def add_Interval(self, distance, totalTime, rest):
    interval = {
      'distance': distance,
      'time': totalTime,
      'rest': rest,
      }
    self.intervals.append(interval) 

  def add_csv(self, csvArray):
    self.intervals = 'No interval data see CSV'
    intervalCount = csvArray[15][0]
    intervals = []

    for x in range(0, int(intervalCount)):
      intervals.append(csvArray[x + 22])

    self.csv = { 
      'type': csvArray[4][1],
      'details': csvArray[2][1],
      'intervalCount': intervalCount,
      'units':csvArray[14],
      'overviewLabels':csvArray[13],
      'overview':csvArray[15],
      'intervalLabels':csvArray[20],
      'intervals':intervals
    }

  def rowFis(self):

    if (self.csv['overview'][14] != None):
      catch = -int(self.csv['overview'][14])
      finish = int(self.csv['overview'][16])
      slip = int(self.csv['overview'][15])
      wash = int(self.csv['overview'][17])
      length = catch + finish

      print(catch, slip, finish, wash, length)

      maleFIS = MaleFIS()
      maleFisQuality = maleFIS.EvalStroke(catch, slip, finish, wash, length)
      femaleFIS = FemaleFIS()
      femaleFISQuality = femaleFIS.EvalStroke(catch, slip, finish, wash, length)

      return {
        'male': maleFisQuality,
        'female': femaleFISQuality
      }  

    else:
      return {
        'male': 'FIS score not available',
        'female': 'FIS score not available'
      }
  
  def addRowFis(self):
    self.maleFis = self.rowFis()['male']
    self.femaleFis = self.rowFis()['female']

  def addToSheets(self):
    try:
      gsheet = GSheet(str(current_user._id))
      gsheet.add_Workout(self)
    except:
      return


  @staticmethod
  def createInterval(distance, time, rest, spm):
    return locals()
  
  @staticmethod 
  def rowFisFromArray(csvArray):
    if (csvArray[15][14] != None):
      catch = -int(csvArray[15][14])
      finish = int(csvArray[15][16])
      slip = int(csvArray[15][15])
      wash = int(csvArray[15][17])
      length = catch + finish

      #print(catch, slip, finish, wash, length)

      maleFIS = MaleFIS()
      maleFisQuality = maleFIS.EvalStroke(catch, slip, finish, wash, length)
      femaleFIS = FemaleFIS()
      femaleFISQuality = femaleFIS.EvalStroke(catch, slip, finish, wash, length)

      return {
        'male': maleFisQuality,
        'female': femaleFISQuality
      }  

    else:
      return {
        'male': 'FIS score not available',
        'female': 'FIS score not available'
      }

  


