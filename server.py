from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

# Here the index.html is a form with a textbox named 'stringEntered'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/', methods=['POST'])
def create_user():
   userKeyedIn = request.form['stringEntered']
   return redirect('/'+userKeyedIn)

@app.route('/<userKeyedIn>')
def show(userKeyedIn):
    return render_template("user.html",thisname=userKeyedIn)

app.run(debug=True)