from app import db
from datetime import datetime, timedelta


class Api(db.Model):
  __tablename__ = 'apis'
  id = db.Column(db.Integer, primary_key=True)
  key = db.Column(db.String(20000), nullable=False)
  ip = db.Column(db.String(300), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Apis %r>' % self.id
