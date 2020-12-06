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
slackEvent = SlackEventAdapter(secret,"/slack/events",server)   #  authenticates provides url for events
bot = slack.WebClient(token=token)
botID = bot.api_call("auth.test")["user_id"]                    #  save bot id so the bot knows if a message is its own

@slackEvent.on("message")                                       #  message.channels event ("event"{"type":"message"})
def message(content):
    event = content.get("event", {})
    channel = event.get("channel")
    user = event.get("user")
    text = event.get("text")

    print(content)                                              #  print entire event (use for log (pipe))

    if(user != botID):                                          #  post a genaric message
        bot.chat_postMessage(channel=channel,text=responses[int(random()*len(responses))])


if(__name__=="__main__"): server.run()                          #  might need to change debug to False
