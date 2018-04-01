from slackclient import SlackClient
import os
import MySQLdb
import json

#tokenFile = open("token_file.txt", "r")
slack_token = os.environ["Slack_token"]
#sc = SlackClient(tokenFile.read())
sc = SlackClient(slack_token)
#tokenFile.close()

def parser(userId, message):
#TODO fix this
    userSkills = []
    Skills = ['C++', 'Javascript', 'Node.js', 'Web Dev', 'Python', 'Ruby', 'Unity', 'Unreal', 'jQuery']
    split_message = message.split()
    for x in range(len(split_message)):
        print "x: " + x
        for y in range(len(Skills)):
            print "y: " + y
            if split_message[x] == Skills[y]:
                print Skills[y]
                userSkills.append(str(Skills[y]))
            #
        #
    userData = sc.api_call (
        "users.info",
        user=userId
    )

    #userData2 = json.JSONDecoder(json.dumps(userData, sort_keys = True, indent = 4))
    a = userData["user"]
    json.JSONDecoder(str(a))
    realName = a["real_name"]
    print realName
    print userSkills
    #add realName to the name category of the final database
    #add userSkills to the skills category of the final database
    return 0

Userid = 'U9U3PSD3K'
Message = "Hello! I am skilled in C++, Javascript, and Python, as well as Unreal Engine 4."
parser(Userid, Message)
