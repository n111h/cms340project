#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  09112020
#  IDEA:  opens questions file and generates questions
################################################################################################################################

####  IMPORTS  #################################################################################################################

####  GLOBALS  #################################################################################################################

questions = []

with open("nameOfQuestionsFile.csv",'r') as questionsFile:
    questionsLines = questionsFile.readlines()

for line in questionsLines[1:]:
    questions.append(line.split(','))

####  FUNCTIONS  ###############################################################################################################

####  MAIN  ####################################################################################################################

def main():
    print(questions)

if(__name__=="__main__"): main()