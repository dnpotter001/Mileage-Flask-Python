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
  
  @staticmethod
  def createInterval(distance, time, rest, spm):
    return locals()


# interval = Workout.createInterval(2000, '6.39', 0, 32)
# print(f'creating intervals {interval}')


