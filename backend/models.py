from peewee import SqliteDatabase, Model, FloatField

db = SqliteDatabase('db.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

class Task(BaseModel):
    download = FloatField()
    upload = FloatField()
    ping = FloatField()