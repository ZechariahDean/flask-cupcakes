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
  return jsonify(cupcakes = all_cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
  """get single cupcake from API"""

  cupcake = Cupcake.query.get_or_404(id)
  return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes", methods = ["POST"])
def add_cupcake():
  """add a cupcake to API"""

  new_cupcake = Cupcake(
    flavor = request.json["flavor"],
    size = request.json["size"],
    rating = request.json["rating"],
    image = request.json["image"] or None)

  db.session.add(new_cupcake)
  db.session.commit()

  response_json = jsonify(cupcake = new_cupcake.serialize())
  return (response_json, 201)

@app.route("/api/cupcakes/<int:id>", methods = ["PATCH"])
def edit_cupcake(id):
  """edit a cupcake in the API"""

  cupcake = Cupcake.query.get_or_404(id)
  cupcake.flavor = request.json["flavor"]
  cupcake.size = request.json["size"]
  cupcake.rating = request.json["rating"]
  cupcake.image = request.json["image"]

  db.session.add(cupcake)
  db.session.commit()

  return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes/<int:id>", methods = ["DELETE"])
def delete_cupcake(id):
  """remove a cupcake from the API"""

  cupcake = Cupcake.query.get_or_404(id)
  db.session.delete(cupcake)
  db.session.commit()

  return jsonify(message = "DELETED")

###################################################################################
# Front end routes
@app.route("/")
def homepage():
  """show homepage"""
  cupcakes = Cupcake.query.all()
  
  return render_template("home.html")
