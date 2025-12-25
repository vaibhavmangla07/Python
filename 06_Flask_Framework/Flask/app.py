from flask import Flask

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World! This is my first Flask application."

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__":
    app.run(debug=True)
