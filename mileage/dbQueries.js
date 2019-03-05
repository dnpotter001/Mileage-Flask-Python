db.users.aggregate([
  {$match: {'_id': ObjectId("5c7e9921c72cf70f380cd763")}},
  {$unwind: {path: "$workouts"}}
])

//returns document for each
db.users.aggregate([
  {$match: {}},
  {$unwind: {path: "$workouts"}},
  {$sort: {"workouts.unixtime":-1}}
])
//returns sorted arrays with display names
db.users.aggregate([
  {$unwind: {path: "$workouts"}},
  {$project: {firstName: 1, lastName: 1, workout: "$workouts"}},
  {$sort: {"workout.unixtime":-1}}
])
//
db.users.aggregate([
  {$unwind: {path: "$workouts"}},
  {$project: {firstName: 1, lastName: 1, workout: "$workouts"}},
  {$sort: {"workout.unixtime":-1}},
  {$limit: 20}
])


db.users.aggregate([
  {$match: {'_id': ObjectId("5c7e9921c72cf70f380cd763")}},
  {$unwind: {path: "$workouts"}},
  {$project: {workout: "$workouts"}},
  {$sort: {"workout.unixtime":-1}},
  {$limit: 20}
])

//all workouts in ordered limited to 20
db.users.aggregate([
  {$unwind: {path: "$workouts"}},
  {$project: {
      _id: "$workouts._id",
      firstName: 1,
      lastName: 1, 
      title: "$workouts.title",
      workoutType: "$workouts.workoutType",
      intervals: "$workouts.intervals",
      csv: "$workouts.csv",
      dateTime: "$workouts.dateTime",
      unixTime: "$workouts.unixtime",
      }},
  {$sort: {"unixTime":-1}},
  {$limit: 20}
])


db.users.aggregate([
  {$unwind: {path: "$workouts"}},
  {$project: {
      _id: "$workouts._id",
      firstName: 1,
      lastName: 1, 
      title: "$workouts.title",
      workoutType: "$workouts.workoutType",
      intervals: "$workouts.intervals",
      csv: "$workouts.csv",
      dateTime: "$workouts.dateTime",
      unixTime: "$workouts.unixtime",
      }},
  {$sort: {"unixTime":-1}},
  {$limit: 20}
])