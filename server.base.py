from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# app.secret_key='use this secret key'
fileName=''
@app.route('/')
def index():
  return render_template('index.html',msg='No ninjas here')
@app.route('/ninja/')
def ninja():
  fileName='tmnt.png';thisMsg='Teenage Mutant Ninja Turtles'
  return render_template('index.html',imgSrc=fileName,useThis=thisMsg)
@app.route('/ninja/<ninja_color>/')
def color(ninja_color):
  if ninja_color=='blue': 
    fileName='leonardo.jpg';thisMsg='Leonardo'
  elif ninja_color=='orange': 
    fileName='michelangelo.jpg';thisMsg='Michaelangelo'
  elif ninja_color=='red': 
    fileName='raphael.jpg';thisMsg='Raphael'
  elif ninja_color=='purple': 
    fileName='donatello.jpg';thisMsg='Donatello'
  else: fileName='notapril.jpg';thisMsg="Not April O'Neil"
  return render_template('index.html',imgSrc=fileName,useThis=thisMsg)

app.run(debug=True)