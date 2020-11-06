#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  05112020
#  IDEA:  this script will listen for a message and respond
################################################################################################################################

####  IMPORTS  #################################################################################################################

from random import random
import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter

####  GLOBALS  #################################################################################################################

token = ""
secret = ""
responses = ["Hey!", "Hi!", "What's up?", "Does this syntax make me look fat?", "That's Tudor to you!", "Genaric response"]

####  FUNCTIONS  ###############################################################################################################

####  MAIN  ####################################################################################################################

server = Flask(__name__)
slackEvent = SlackEventAdapter(secret,"/slack/events",server)
bot = slack.WebClient(token=token)
botID = bot.api_call("auth.test")["user_id"]

@slackEvent.on("message")
def message(content):
    event = content.get("event", {})
    channel = event.get("channel")
    user = event.get("user")
    text = event.get("text")

    print(content)

    if(user != botID):
        bot.chat_postMessage(channel=channel,text=responses[int(random()*len(responses))])


if(__name__=="__main__"): server.run(debug=True)
