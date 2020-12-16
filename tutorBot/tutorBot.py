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
from tutorParser import callSplit
from tutorQuestions import generate_questions

####  GLOBALS  #################################################################################################################

token = ""
secret = ""
#responses = ["Hey!", "Hi!", "What's up?", "Does this syntax make me look fat?", "That's Tudor to you!", "Genaric response"]
conversations = {}

####  FUNCTIONS  ###############################################################################################################

def questionUnpacker(q):
    qText = q["Question"]
    if(str(q['A']) != "nan"):
        qText += ("\nA. " + str(q['A']))
    if(str(q['B']) != "nan"):
        qText += ("\nB. " + str(q['B']))
    if(str(q['C']) != "nan"):
        qText += ("\nC. " + str(q['C']))
    if(str(q['D']) != "nan"):
        qText += ("\nD. " + str(q['D']))
    return(qText)

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
    
    print(content,event,channel,user,text,sep='\n')                                                            ##  DEBUGGING  ##

    if(user != botID):
        if(user not in conversations):                          #  first message/welcome
            welcome = "Welcome to the tutor bot - message code blocks to generate questions"
            bot.chat_postMessage(channel=channel,text=welcome)
            conversations[user] = [False,[],[text,welcome]]
        elif("```" in text):                                    #  code block in message
            textSplit = text.split("```")
            if(len(textSplit) == 3):                            #  single code block
                codeLines = callSplit(textSplit[1])             #  parse code bloack with tutorParser
                #print(codeLines)                                                                               ##  DEBUGGING  ##
                conversations[user][1] = generate_questions(codeLines)          #  geneate and save list of questions
                if(len(conversations[user][1]) > 0):            #  tutorQuestions was able to generate questions
                    question = conversations[user][1].pop(0)    #  if there are questions pop the first one into question
                    conversations[user][0] = question["Answer"] #  set the answer in user conversation value
                    questionText = questionUnpacker(question)   #  unpack question text into string
                    print('',conversations[user][0],question,'',sep='\n')                                     ##  DEBUGGING  ##
                else:                                           #  tutorQuestions failed to generate questions
                    conversations[user][0] = 'A'                                #  for debugging (really want ans letter)
                    questionText = "test question (answer A) A. B. C. D."       #  for debugging (really want question text)
                conversations[user][2].append(text)
                conversations[user][2].append(questionText)
                bot.chat_postMessage(channel=channel,text=questionText)
            else:                                               #  unexpected number of code blocks
                textError = "I'm sorry, I couldn't find your code"
                conversations[user][2].append(text)
                conversations[user][2].append(textError)
                conversations[user][0] = False
                bot.chat_postMessage(channel=channel,text=textError)
        elif(conversations[user][0]):                           #  value (or, not False) in index 0 (answer)
            if(conversations[user][0] in text.upper()):         #  answer letter in message text
                correct = "That's correct!"
                conversations[user][2].append(text)
                conversations[user][2].append(correct)
                bot.chat_postMessage(channel=channel,text=correct)
                if(len(conversations[user][1]) > 0):            #  if there are still questions to ask
                    question = conversations[user][1].pop(0)
                    conversations[user][0] = question["Answer"] #  set the answer in user conversation value
                    questionText = questionUnpacker(question)   #  unpack question text into string
                    print('',conversations[user][0],question,'',sep='\n')                                     ##  DEBUGGING  ##
                    conversations[user][2].append(text)
                    conversations[user][2].append(questionText)
                    bot.chat_postMessage(channel=channel,text=questionText)
                else:                                           #  no questions left to ask
                    prompt = "Post a code block to generate questions"
                    conversations[user][2].append(text)
                    conversations[user][2].append(prompt)
                    conversations[user][0] = False
                    bot.chat_postMessage(channel=channel,text=prompt)
            else:
                incorrect = "I'm sorry, I don't think that's right."
                conversations[user][2].append(text)
                conversations[user][2].append(incorrect)
                bot.chat_postMessage(channel=channel,text=incorrect)
                if(len(conversations[user][1]) > 0):            #  if there are still questions to ask
                    question = conversations[user][1].pop(0)
                    conversations[user][0] = question["Answer"] #  set the answer in user conversation value
                    questionText = questionUnpacker(question)   #  unpack question text into string
                    print('',conversations[user][0],question,'',sep='\n')                                     ##  DEBUGGING  ##
                    conversations[user][2].append(text)
                    conversations[user][2].append(questionText)
                    bot.chat_postMessage(channel=channel,text=questionText)
                else:                                           #  no questions left to ask
                    prompt = "Post a code block to generate questions"
                    conversations[user][2].append(text)
                    conversations[user][2].append(prompt)
                    conversations[user][0] = False
                    bot.chat_postMessage(channel=channel,text=prompt)
        else:                                                   #  no code block in message, or question posed - prompt
            prompt = "Post a code block to generate questions"
            conversations[user][2].append(text)
            conversations[user][2].append(prompt)
            conversations[user][0] = False
            bot.chat_postMessage(channel=channel,text=prompt)

        #bot.chat_postMessage(channel=channel,text=(responses[int(random()*len(responses))]),)
            

# @slackEvent.on("app_mention")
# def mention(content):
#     event = content.get("event", {})
#     print(content,event,sep='\n')

#     channel = event.get("channel")
#     user = event.get("user")

#     bot.chat_postEphemeral(channel=channel,text="this is a response to a message",user=user,blocks=block)


# @slackEvent.on("message.app_home")
# def privateMessage(content):
#     event = content.get("event", {})
#     print(content,event,sep='\n')

#     channel = event.get("channel")
#     user = event.get("user")

#     bot.chat_postEphemeral(channel=channel,text="this is a response to a message",user=user,blocks=block)


if(__name__=="__main__"): server.run()                          #  might need to change debug to False
