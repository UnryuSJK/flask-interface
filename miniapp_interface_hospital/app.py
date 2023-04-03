import json
from templates.utils import patient_list

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/patient_register', methods=['GET', 'POST'])
def patient_register():
    if request.method == 'GET':
        patient_info = json.loads(request.get_data())
        print(patient_info)
        # print(patient_list.add_patient(patient_info))
        return patient_list.add_patient(patient_info)
    pass


@app.route('/patient_login', methods=['GET'])
def patient_login():

    pass


if __name__ == '__main__':
    app.run()
