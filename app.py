"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'

connect_db(app)

with app.app_context():
  db.create_all()

################################################################
# Routes for API
@app.route("/api/cupcakes")
def get_cupcakes():
  """get list of cupcakes from API"""

  all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
  return jsonify()