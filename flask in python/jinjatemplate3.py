#A variable rule in Flask allows you to pass dynamic values in the URL.
"""
/score/90
/score/45
/score/100
"""
from flask import Flask,render_template,redirect,url_for,request

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
@app.route("/successif/<int:marks>")
def successif(marks):
    
    return render_template("score2.html",marks=marks)
@app.route("/submit",methods=["GET","POST"])
def submit():
    total_marks=0
    if request.method=="POST":
        ds=float(request.form['ds'])
        ai=float(request.form['ai'])
        ml=float(request.form['ml'])
        python=float(request.form['python'])
        total_score=(ai+ml+ds+python)/4
        return render_template("score2.html",marks=total_score)
    return render_template("submit.html")
if __name__=="__main__":
    app.run(debug=True)
