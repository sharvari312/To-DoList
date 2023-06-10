from app import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.String(200))
    priority=db.Column(db.String(100))
    date_created=db.Column(db.DateTime,default=datetime.utcnow)


if __name__ == "__main__":
    app.run(debug=True)