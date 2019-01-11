from flask import Flask, render_template, url_for
app = Flask(__name__)

workouts = [
  {
    'author':'David Potter',
    'title': 'Sunday workout',
    'date': '11th Jan 2029'
  },
  {
    'author':'Judith Potter',
    'title': 'Saturday workout',
    'date': '12th Jan 2029'
  }
]

@app.route("/")
@app.route("/home")
@app.route("/feed")
@app.route("/index")
def home():
    return render_template('index.html', posts=workouts, title="Your Feed")

@app.route("/about")
def about():
  return  render_template('about.html', title="About")

if __name__ == '__main__':
  app.run(debug=True)
