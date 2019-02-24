import datetime
from bson import ObjectId

class Workout(object):

  def __init__(self, title, workoutType):
    self._id = ObjectId()
    self.title = title
    self.workoutType = workoutType
    self.intervals = []
    self.dateTime = datetime.datetime.today().strftime('%Y-%m-%d')

  def add_Interval(self, distance, totalTime, rest):
    interval = {
      'distance': distance,
      'time': totalTime,
      'rest': rest,
      }
    self.intervals.append(interval) 

  def add_csv(self, csvArray):
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

  @staticmethod
  def createInterval(distance, time, rest, spm):
    return locals()

  


