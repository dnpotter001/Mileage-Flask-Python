
class Workout(object):

  def __init__(self, date, time, title):
    self.title = title
    self.date = date
    self.time = time
    self.intervals = []

  def singleInterval(self, distance, workoutTime, spm):
    self.intervals = (distance, workoutTime, spm)

  def add_Interval(self, distance, totalTime, rest):
    interval = {
      'distance': distance,
      'time': totalTime,
      'rest': rest,
      }
    self.intervals.append(interval) 
  
  @staticmethod
  def createInterval(distance, time, rest, spm):
    keys = locals()
    values = (distance, time, rest, spm)
    interval = dict(zip(keys, values))
    return interval

interval = Workout.createInterval(2000, '6.39', 0, 32)
print(interval)

workout = Workout('today', 'now', 'workout')
workout.singleInterval(2000, '6.39', 32)
print(workout.__dict__)
