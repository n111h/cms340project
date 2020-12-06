#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  09112020
#  IDEA:  holds parsing funcion
################################################################################################################################

####  IMPORTS  #################################################################################################################

####  GLOBALS  #################################################################################################################

####  FUNCTIONS  ###############################################################################################################

def parser(snippet):                                            #  takes a string as a arg (assumed to have ``` pre-stripped)
    variables = {}                                              #  a dict containing var names as keys and values as values
    lines = snippet.split('\n')                                 #  split the snippet into it's lines
    for line in lines:                                          #  iterate over the lines in the code snippet
        tokens = [t for t in line.split(' ') if t != '']        #  create an array of tokens (anything other than white-space)
        #print(tokens)                                                                                         ##  DEBUGGING  ##
        for index,token in enumerate(tokens):
            #print(index,token)                                                                                ##  DEBUGGING  ##
            if(token=='='):
                variables[tokens[(index-1)]] = tokens[(index+1)]#  saves the token after '=' to variables[token before '=']

    return(variables)

####  MAIN  ####################################################################################################################

def main():
    testSnippet = "x = 5\ny = 3.1415\nz = 'string'\n"
    print(parser(testSnippet))

if(__name__=="__main__"): main()
