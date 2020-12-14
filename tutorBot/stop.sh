#!/bin/bash

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  07112020
#  IDEA:  this script will close the port used for the tutor flask server
################################################################################################################################

echo "" | sudo -S ufw deny 5000                                 #  pipes user pwd to sudo to close port 5000 in firewall
