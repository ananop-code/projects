from ext import db

class History(db.Model):
    __tablename__ = "histories"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    image = db.Column(db.String(), default="default_image.jpg")