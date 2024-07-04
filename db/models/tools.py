from ..database import db


class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)