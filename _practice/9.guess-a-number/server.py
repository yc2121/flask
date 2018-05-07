from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# app.secret_key='a secret key here'

import os, random
app.secret_key=os.urandom(24).encode('hex')

@app.route('/', methods=['GET','POST'])
def index():
  if 'reset' in session:
    session['theNumber']=random.randrange(0, 101) # random number between 0-100
    session.pop('msg')
    session.pop('reset')    
  elif 'theNumber' in session:
    if request.method=='POST':
      if request.form['guess'].isdigit():
        x = int(request.form['guess'])
        if x < session['theNumber']:
          session['msg']='Too low!'
        elif x == session['theNumber']:
          session['msg']=str(session['theNumber'])+" was the number!"
          session['reset']=True
        else:
          session['msg']='Too high!'
      else:
        session['msg']='Only digits, please'
  else:
    session['theNumber']=random.randrange(0, 101) # random number between 0-100
  return render_template('index.html')

app.run(debug=True)