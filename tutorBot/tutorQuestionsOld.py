#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  09112020
#  IDEA:  opens questions file and generates questions
#       There are certain types of questions that must be created depending on the syntax error that they make or 
#       what they implement within the codeblock. For example, syntax question about the indentation is always created when user 
#       used wrong indentation. 

################################################################################################################################

####  IMPORTS  #################################################################################################################
import pandas as pd
from random import randint, choice
from ast import literal_eval

####  GLOBALS  #################################################################################################################
question_df = pd.read_csv('Questions_11_27.csv')
existing_q_id = []
syntax_list = ['def','if','else','==','+','-','*','/',"'",'"']
data_types = ['int','str','float','bool','list']
                                                                                                   # we are using a python libary called Pandas to manipulate the
                                                                                                   # csv file easily by creating a pandas dataframe. 
                                                                                                   # .set_index would make one of the column in the csv file
                                                                                                   # 'Question Type' as index and we can extract the matching   
                                                                                                   # question according to the input we'll receive
                                                                                                   


####  FUNCTIONS  ###############################################################################################################
################################################################################################################################
#### check_question ############################################################################################################

# Input: list of questions 
# Output list that contains question id
# Objective: iterate through the list of questions created and record the existing_question_id so that we can keep track of what questions can be created and 
# what questions should not be created


def check_question(questions):
    
    existing_q_id = list()
    
    if len(questions) == 0:                                                                        # if the questions list is empty, return a list with 0
        return [0]
    else:                                                                                          # if the questions list is not empty,
        
        for q in questions:                                                                        # iterate throught the list of questions
            existing_q_id.append(q['id'])
    
    return existing_q_id
    
    

################################################################################################################################
#### check_indent function #####################################################################################################

# Input: two dimensional list
# Output: boolean
# Objective: iterate through the two dimensional list and make sure there is no error with indentation
# Returning True indicate that there is no indentation issue, and False represents an issue with spaces

def check_indent(lines):
    
    # local variable flag, if anything weird didn't happen then this function will return True
    flag = True
    
    for line in range(len(lines)):                                                                 # iterating through the 2-d list
        
        cur = lines[line]

        if (cur[0] % 4 != 0):                                                                      # if the number of space is not multiple of 4

            flag = False                                                                           # this is the base case that can be applied to either a single
            break                                                                                  # line of code or multiple lines of code. 
        
        
        if len(lines) > 1:                                                                         # if the code was not a single line. 
            
            # get the previous lines
            prev = lines[line - 1]
            
            if ((prev[len(prev)-1] == ':') and (cur[0] != (prev[0] + 4))):                         # the previous line ends with : but the number of space is not
                                                                                                   # incremented by 4
                flag = False
                break
    
    
    return flag

################################################################################################################################
#### create_iData_type function ################################################################################################

# Input: list which is the entire row in the two-d list and an int which is an index of '='
# Output: dictionary which is a question, and choices and its answer and link to the feedback
# Objective: create a iData type question

def create_iData_type(line, index):
    
    # get the iData_type question as dictionary
    question = question_df.set_index('Question Type').loc['iData Types'].to_dict()
    question_df.reset_index()
    print(question)                                                                                # debugging
    choices = data_types
    answer = question['Answer']
    print(choices)                                                                                 # debugging
    # list to keep track of data type that was chosen as the 
    chosen = []

    # getting the variable name and getting the data_type of variable. 
    variable_name = line[index - 1]
    variable_type = type(literal_eval(line[index + 1]))

    # print(variable_name, variable_type)                                                          # debugging 
    
    if variable_type == str:

        # modifying the question choice to avoid overlap
        answer = 'str'
        
        
    if variable_type == int:
        answer = 'int'

        
    if variable_type == float:
        answer = 'float'
        
    if variable_type == bool:
        answer = 'boolean'

    if variable_type == list:
        answer = 'list'
        
    print("Answer", answer)
    
    # using ascii value, selecting the key to put the answer and place the answer. 
    answer_key = chr(65 + randint(0,3))
    chosen.append(answer)
    question[answer_key] = answer
    question['Answer'] = answer_key
    print("Printing chosen", chosen)
    
    # selecting the rest of the answers. 
    for i in range(3):
        
        key = chr(65 + randint(0,3))
        
        while key == answer_key:
            key = chr(65 + randint(0,3))
            
        
        dummy = choice(choices)
        
        while dummy in chosen:
            dummy = choice(choices)
        
        chosen.append(dummy)
        question[key] = dummy
        
    
    # modify the question sentence
    question['Question'] = question['Question'].replace("(variable name)",variable_name)
    
    return question


################################################################################################################################

"""This function is going to create a set of questions  """

# Input: two dimensional list called term_lists
#        the first index, the row represents the line, second index columns are the terms on that line. 
# Output: two dimensiocal list which contains a list of questions and answer keys. 

def generate_questions(term_lists):
    
    questions = list()
    iData_type = False
    Generic = False
    
    # have a for loop to create randomly selected 7 questions and append to the questions list
    # first we could check for line indentation which is the very important and simple syntax question we can ask
    indentation = check_indent(term_lists)
    
    # if we see the flag being False, append the syntax question about the indentation/spaces
    if (indentation == False):
        q = question_df.set_index('Question Type').loc['Syntax'].iloc[4].to_dict()
        questions.append(q)                                                                        # set_index is going to use certain column as index of the
                                                                                                   # pandas dataframe which is id in this case, and we know the
                                                                                                   # id for the indentation syntax so we get the question by
                                                                                                   # loc[] operator and preserve the entire row as a list.
    # going through the two dimensional list again
    # we will visit each line to create data type question, or syntax question, or generic question
    
    
    for line in range(len(term_lists)):
        # question = generate_question(questions, tokens)
        # we first want to make sure what questions are already in the list of questions
        existing_q_id = check_question(questions)
        # get the current line of code
        current = term_lists[line]
        print('Current line:', current)
        # we will have an internal for loop to go through each terms except the first elements which indicates the number of spaces.  
        
        for term in range(1,len(current)):
            
            t = current[term]
            
            if (t == '=' and iData_type == False):
                # create iData_type_qestion
                question = create_iData_type(current, term)
                iData_type = True
                questions.append(question)
                continue
            
            if (t == '=' and iData_type == True):
                # print('Creating data type question')          
                # create a data type question.
                
                dtq = question_df.set_index('Question Type').loc['Data Types']
                question_df.reset_index()
                question = dtq.iloc[randint(0, len(dtq) - 1)]
                
                
                while question['id'] in existing_q_id:
                    question = dtq.iloc[randint(0, len(dtq) - 1)]
                   
                    q = question.to_dict()
                
                q = question.to_dict()
                questions.append(question)
                continue
            
            if (t in syntax_list):
                
                # create syntax question
                
                stq = question_df.set_index('Question Type').loc['Syntax']
                question_df.reset_index()
                question = stq.iloc[randint(0, len(stq) - 1)]
                
                while question['id'] in existing_q_id:
                    question = stq.iloc[randint(0, len(stq) - 1)]
                    
                 
                q = question.to_dict()
                questions.append(question)
                continue
        
        
        
        
        # check if we reached the number of questions we wanted. 
        
        if len(questions) == 4:
            break
    
    # after going through everything and you don't have enough question, add one generic question.
    if len(questions) < 4:
        
        gnq = question_df.set_index('Question Type').loc['Generic']
        question_df.reset_index()
        question = gnq.iloc[randint(0, len(gnq) - 1)].to_dict()
        questions.append(question)
        
    return questions



####  MAIN  ####################################################################################################################

def main():
    print(questions)

if(__name__=="__main__"): main()
