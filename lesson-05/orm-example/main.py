from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///localhost.sqlite")


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    username = db.Column(db.String)


db.create_all()  # this creates the tables (unless it's already created). It does not override any table already created.


# message = Message(text="Hello world! :)")
# db.add(message)
# db.commit()

message_2 = Message(text="Hey hey hey!", username="Carlos")
db.add(message_2)
db.commit()

messages = db.query(Message).all()

for row in messages:
    print(row.text)


message_first = db.query(Message).first()
print(message_first.text)
