from flask import Flask
import csv
import pathlib
from pprint import pprint
from flask import send_file

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong'

@app.route('/system-info')
def system_info():
    path = pathlib.Path("/etc/os-release")
    with open(path) as stream:
      reader = csv.reader(stream, delimiter="=")
      os_release = dict(reader)
    return os_release

@app.route('/home')
def home():
    return send_file('../mydata/image1.jpg') 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
