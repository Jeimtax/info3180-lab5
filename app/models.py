from app import db
from datetime import datetime

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

