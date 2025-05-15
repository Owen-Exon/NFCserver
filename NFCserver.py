from flask import Flask
from ahk import AHK
import os

ahk = AHK()
app = Flask(__name__)

@app.route('/go', methods=['GET'])
def go():
    os.popen('start "" "https://www.google.com"')
    return "Success" , 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')