"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cupcake(db.Model):
  """model for cupcake database"""

  __tablename__ = "cupcakes"

  id = db.Column(db.Integer, primary_key = True)
  flavor = db.Column(db.Text, nullable = False)
  size = db.Column(db.Text, nullable = False)
  rating = db.Column(db.Float, nullable = False)
  image = db.Column(db.Text, nullable = False, default = "https://tinyurl.com/demo-cupcake")

  def serialize(self):
    """create serialized information"""
    info = {
      "id": self.id,
      "flavor": self.flavor,
      "size": self.size,
      "rating": self.rating,
      "image": self.image,
    }
    return info


def connect_db(app):
  """Connect the database to application"""
  db.app = app
  db.init_app(app)