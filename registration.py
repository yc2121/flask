from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='use this secret key'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/', methods=['POST'])
def process():
  if len(request.form['nameEntered'])<1:
    flash('Name cannot be blank!')
    return redirect("/")
  elif len(request.form['commentEntered'])>120:
    flash('Please keep your comment within 120 characters.')
    return redirect("/")
  else:
    session['name']    = request.form['nameEntered']
    session['location']= request.form['locationPicked']
    session['language']= request.form['languagePicked']
    session['comment'] = request.form['commentEntered']
    flash('Login successgul.')
  return redirect('/result')

@app.route('/result')
def result():
    return render_template(
      "result.html"
      ,name=session['name']
      ,location=session['location']
      ,language=session['language']
      ,comment=session['comment']
      )

app.run(debug=True)