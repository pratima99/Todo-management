from extensions import db
from datetime import datetime


class Todo(db.Document):
    title = db.StringField(required=True)
    time = db.DateTimeField(required=True, default=datetime.now)

