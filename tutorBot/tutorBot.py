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
block = '{"text": "Question text","fallback":"Question text fallback","callback_id":"question_id","attachment_type":"default",'
block += '"actions":[{"name":"ans","text":"A","type":"button","value":"a"}{"name":"ans","text":"B","type":"button","value":"b"}'

####  FUNCTIONS  ###############################################################################################################

####  MAIN  ####################################################################################################################

server = Flask(__name__)
slackEvent = SlackEventAdapter(secret,"/slack/events",server)   #  authenticates provides url for events
bot = slack.WebClient(token=token)
botID = bot.api_call("auth.test")["user_id"]                    #  save bot id so the bot knows if a message is its own

@slackEvent.on("message")                                       #  message.channels event ("event"{"type":"message"})
def message(content):
    event = content.get("event", {})
    print(content,event,sep='\n')                               #  print entire event (use for log (pipe))

    channel = event.get("channel")
    user = event.get("user")

    if(user != botID):                                          #  post a genaric message
        bot.chat_postMessage(channel=channel,text=(responses[int(random()*len(responses))]),)
            

@slackEvent.on("app_mention")
def mention(content):
    event = content.get("event", {})
    print(content,event,sep='\n')

    channel = event.get("channel")
    user = event.get("user")

    bot.chat_postEphemeral(channel=channel,text="this is a response to a message",user=user,blocks=block)


@slackEvent.on("message.app_home")
def privateMessage(content):
    event = content.get("event", {})
    print(content,event,sep='\n')

    channel = event.get("channel")
    user = event.get("user")

    bot.chat_postEphemeral(channel=channel,text="this is a response to a message",user=user,blocks=block)


if(__name__=="__main__"): server.run()                          #  might need to change debug to False
