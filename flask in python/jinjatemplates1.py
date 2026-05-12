#A variable rule in Flask allows you to pass dynamic values in the URL.
"""
/score/90
/score/45
/score/100
"""
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to homepage"
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/test")
def test():
    return "FLASK IS WORKING"
@app.route("/score_html/<int:marks>")
def score_html(marks):
    res=""
    if marks>50:
        res="PASSED"
    else:
        res="FAIL"
    # marks is received as an integer from the URL
    # str(marks) converts integer to string for concatenation
    return render_template("score.html",scores=res)
@app.route("/scoreres/<int:marks>")
def scoreres(marks):
    res=""
    if marks>50:
        res="PASSED"
    else:
        res="FAIL"
    exp={"marks":marks,'res':res}
    # marks is received as an integer from the URL
    # str(marks) converts integer to string for concatenation
    return render_template("score1.html",scoreres=exp)
if __name__=="__main__":
    app.run(debug="True")
