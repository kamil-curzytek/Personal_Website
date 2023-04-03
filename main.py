#importing Flask class from flask framework
from flask import Flask

#to use html files and display it in the requested URL
from flask import render_template

#flask object with value of the python script name, when we execture the script Python assignes __name__ => __main__
app = Flask(__name__)

#output will be mapped to this URL, e.g. /about/ etc.
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/education/')
def education():
    return render_template("education.html")

@app.route('/skills/')
def skills():
    return render_template("skills.html")

@app.route('/projects/')
def projects():
    return render_template("projects.html")    

@app.route('/experience/')
def experience():
    return render_template("experience.html")

#script control if it's executed or imported
if __name__ == '__main__':
    app.run(debug=True)

