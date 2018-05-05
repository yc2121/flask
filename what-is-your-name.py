from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/', methods=['POST'])
def process():
  print 'HI'
  session['username']=request.form['username']
  print session['username']
  return redirect('/'+session['username'])

app.run(debug=True)