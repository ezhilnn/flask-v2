from flask import Flask,render_template
app = Flask(__name__)
JOBS = [
    {'id': 1, 'title': 'Python Developer', 'location': 'New York', 'salary': '$100000'},
    {'id': 2, 'title': 'Java Developer', 'location': 'San Francisco', 'salary': '$110000'},
    {'id': 3, 'title': 'Web Developer', 'location': 'Chicago', 'salary': '$95000'},
    {'id': 4, 'title': 'Software Engineer', 'location': 'Seattle', 'salary': '$105000'}
]
@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)