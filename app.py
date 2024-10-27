from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)


class RoomRequest(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    room = db.Column(db.String(40), nullable=False)
    reason = db.Column(db.String(500))
    date = db.Column(db.String(40))
with app.app_context():
    db.create_all()
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/bubble', methods=['POST'])
def parse_request():
    data = request.data  # data is empty
    # need posted data here
    my_dict = request.form.to_dict()
    if "Room" not in my_dict or "Date" not in my_dict:
        abort(400)
    room_request = RoomRequest(room = my_dict["Room"], date = my_dict["Date"])
    room_request.reason = my_dict["Reason"]
    db.session.add(room_request)
    db.session.commit()
    print(str(my_dict['Room']))
    print(str(my_dict['Date']))
    print(str(my_dict['Reason']))
    return str(room_request.ID)
@app.route('/bubble', methods=['GET'])
def bubble():
    my_dict = request.form.to_dict()
    ID = my_dict["ID"]
    room_request = db.session.execute(db.select(RoomRequest).filter_by(ID=ID)).scalar_one_or_none()
    if room_request is None: abort(418)
    return room_request.date


@app.route('/bubble', methods=['DELETE'])
def water():
    my_dict = request.form.to_dict()
    ID = my_dict["ID"]
    room_request = db.session.execute(db.select(RoomRequest).filter_by(ID=ID)).scalar_one_or_none()
    if room_request is None: abort(418)
    db.session.delete(room_request)
    db.session.commit()
    return 'success'

if __name__ == '__main__':
    app.run()





