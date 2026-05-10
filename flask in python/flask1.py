from flask import Flask

# WSGI framework
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask in Python,this is complete course"

@app.route("/index")
def index():
    return "Welcome to index"

if __name__ == "__main__":
    app.run(debug=True)