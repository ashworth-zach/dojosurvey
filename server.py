# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['firstname']) < 1:
        flash(u"name cannot be blank!", 'errorname')
    if len(request.form['message']) < 1:
        flash(u"message field cannot be blank!", 'error')
    if len(request.form['message'])>120:
        flash(u'message is too long!', 'error')
    elif len(request.form['firstname']) > 0 and len(request.form['message']) > 0 and len(request.form['message'])<120:
        flash("Success!")
        session['message']=request.form['message']
        session['firstname']=request.form['firstname']
        session['location']=request.form['location'] 
        session['language']=request.form['language']
        return redirect('/result')
    return redirect('/')


@app.route('/result')
def result():
    return render_template('result.html', message=session['message'], firstname=session['firstname'], location = session['location'], language=session['language'])
if __name__=="__main__":
    app.run(debug=True)
