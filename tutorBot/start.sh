#!/bin/bash

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  07112020
#  IDEA:  this script will start the tutor flask server and open the appropriate ports in the firewall
################################################################################################################################

echo "" | sudo -S ufw allow 5000                                #  pipes user pwd to sudo to open port 5000 in firewall     
export FLASK_APP=/slack/tutorBot.py                             #  sets env vairable for flask to tutorBot script
flask run --host=0.0.0.0                                        #  runs flask server as publicly available
