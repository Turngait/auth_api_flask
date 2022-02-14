from app import db
from datetime import datetime, timedelta


class Session(db.Model):
  __tablename__ = 'sessions'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String(20000), nullable=False)
  token = db.Column(db.String(300), nullable=False)
  expired_at = db.Column(db.DateTime, default=datetime.today() + timedelta(days=7))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<User %r>' % self.id
