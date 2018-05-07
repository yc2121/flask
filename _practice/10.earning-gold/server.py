from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

import os, random, datetime
app.secret_key=os.urandom(24).encode('hex')

@app.route('/')
def index():
  if not 'gold' in session:
    session['gold']=0
    session['history']={}
  return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
  if request.form['building']=='Farm':
    x=random.randrange(10,21); session['gold']+=x
    msg='Earned '+str(x)+' golds from the fram! ('+str(datetime.datetime.now())+')'
  elif request.form['building']=='Cave':
    x=random.randrange(5,11); session['gold']+=x
    msg='Earned '+str(x)+' golds from the Cave! ('+str(datetime.datetime.now())+')'
  elif request.form['building']=='House':
    x=random.randrange(2,6); session['gold']+=x
    msg='Earned '+str(x)+' golds from the House! ('+str(datetime.datetime.now())+')'
  else:
    a='Earned a casino and '
    x=random.randrange(-50,50); session['gold']+=x
    if x>0:
      b='earned';c='YES...'
    else:
      b='lost';c='Ouch...'
    msg=a+b+str(x)+' golds...'+c+'('+str(datetime.datetime.now())+')'
  session['history']=msg
  return redirect('/')

app.run(debug=True)