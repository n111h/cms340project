#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  03112020
#  IDEA:  this script will post a basic message to the slack channel #tutoring-Bot
################################################################################################################################

####  IMPORTS  #################################################################################################################

import slack
import os
from pathlib import Path
from dotenv import load_dotenv

####  GLOBALS  #################################################################################################################

env = Path('.')/".env"

####  FUNCTIONS  ###############################################################################################################

####  MAIN  ####################################################################################################################

load_dotenv(dotenv_path=env)

bot = slack.WebClient(token=os.environ["TOKEN"])

bot.chat_postMessage(channel="#tutoring-bot",text="Hello World\nI come from python3 running on a cloud server!")