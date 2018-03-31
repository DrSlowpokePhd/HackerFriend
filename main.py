from slackclient import SlackClient
import os
import json

slack_token = os.environ["Slack_token"]
sc = SlackClient(slack_token)

info = sc.api_call(
    "channels.history",
    channel='C9S7YCHJS',
    count=1000
)
object = open('team_history.json', 'w')
object.write(json.dumps(info, sort_keys = True, indent = 4))#str(info))

#RTM Connection code
#if sc.rtm_connect():
# while sc.server.connected is True:
#        print sc.rtm_read()
#        time.sleep(1)
#else:
#    print "Connection Failed"
