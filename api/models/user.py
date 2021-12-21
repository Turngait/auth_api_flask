from app import db
from datetime import datetime


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(300), nullable=False)
  paper = db.Column(db.String(300))
  name = db.Column(db.String(100), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<User %r>' % self.id
