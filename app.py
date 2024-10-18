from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# db = SQLAlchemy(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/bubble', methods=['GET', 'POST'])
def parse_request():
    data = request.data  # data is empty
    # need posted data here
    my_dict = request.form.to_dict()
    if "Room" not in my_dict or "Date" not in my_dict:
        abort(400)
    print(str(my_dict['Room']))
    print(str(my_dict['Date']))
    print(str(my_dict['Reason']))
    return str(my_dict['Date'])


if __name__ == '__main__':
    app.run()





