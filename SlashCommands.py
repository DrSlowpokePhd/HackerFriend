from flask import Flask
from slackclient import SlackClient
import os
import MySQLdb
import json
app = Flask(__name__)

@app.route("/", methods=['POST'])

slack_token = os.environ["Slack_token"]
sc = SlackClient(slack_token)





def sortData(arg):


def findteam():
    return "here is a list of qualified partners calculated and served here on a silver platter\n"
#db = MySQL.connect()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
