from flask import Flask
from slackclient import SlackClient
import os
app = Flask(__name__)

@app.route("/", methods=['POST'])

#Skills = ['C ', 'C++', 'Java ', 'Javascript', 'JS', 'Node', 'Web Dev', 'Python', 'Ruby', 'Unity', 'Unreal', ]

def findteam():
    return "list of qualified partners calculated and served here on a silver platter\n"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
