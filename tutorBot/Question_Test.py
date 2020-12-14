import unittest
from tutor_Question import check_question, check_indent, create_iData_type, generate_questions


# UnitTesting for our components and its functions. 

class Test_tutor_Question(unittest.TestCase):
    
    def test_check_question_empty(self):
        
        data = []
        
        result = check_question(data)
        self.assertEqual(result, [0])
    
    def test_check_question_single(self):
        
        data = list()
        # example of question that could be created. 
        q = {'id': 1, 'Question': 'what is the data type of (variable name)?', 'A': 'int', 'B': 'float', 'C': 'str', 'D': 'bool', 'Answer': 'TBD', 'Link': 'http://greenteapress.com/thinkpython/html/thinkpython003.html#toc12'}
        data.append(q)
        
        result = check_question(data)
        
        self.assertEqual(result,[1])
        
    def test_check_question_multiple(self):
        
        data = []
        
        # two examples of questions 
        q = {'id': 1, 'Question': 'what is the data type of (variable name)?', 'A': 'int', 'B': 'float', 'C': 'str', 'D': 'bool', 'Answer': 'TBD', 'Link': 'http://greenteapress.com/thinkpython/html/thinkpython003.html#toc12'}
        q2 = {'id': 10, 'Question': 'Is indentation important in Python?', 'A': 'Yes it is important because it would make my code look nicer', 'B': 'Yes it is very important so that we and python can identify code blocks', 'C': "No, Python doesn't care, they can handle anything", 'D': 'No, because we can use semicolons and parentheses', 'Answer': 'B', 'Link': ""}
        data.append(q)
        data.append(q2)
        
        result = check_question(data)
        
        self.assertEqual(result,[1,10])

    def test_check_indent(self):
        
        data = [ [0,'def','hello', '(',')',':'],
                 [4, 'print','(','"hello"',')']
            ]
        result = check_indent(data)
        
        self.assertEqual(result, True)
        
    def test_check_indent_single_line(self):
        
        data = [[0,'x', '=', '9']]
        result = check_indent(data)
        
        self.assertEqual(result, True)
    
    def test_check_indent_flag_single(self):
        
        data = [[2,'x', '=', '9']]
        result = check_indent(data)
        self.assertEqual(result, False)
        
    def test_check_indent_flag(self):
        
        data = [ [0,'def','hello', '(',')',':'],
                 [5, 'print','(','"hello"',')']
            ]
            
        result = check_indent(data)
        self.assertEqual(result, False)
        
    def test_check_indent(self):
        
        data = [ [0,'def','hello', '(',')',':'],
                 [4, 'print','(','"hello"',')']
            ]
        result = check_indent(data)
        self.assertEqual(result, True)
    
    # check if the function really created the create_iData_type question. 
    # Given that the id of the only iData_type question is 1. we can test the function by checking the id of question generated. 
    
    def test_create_iData_type(self):
        
        data = [0,'x', '=', '9']
        result = create_iData_type(data, 2)
        
        q_type = result['id']
        self.assertEqual(q_type, 1)
    
    def test_create_iData_type_int(self):
        
        data = [0,'x', '=', '9']
        result = create_iData_type(data, 2)
        
        a_key = result['Answer']
        answer = result[a_key]
        
        self.assertEqual(answer, 'int')
    
    # def test_create_iData_type_list(self):
        
    #     data 
    
    def test_create_iData_type_bool(self):
        
        data = [0, 'x', '=', 'True']
        
        result = create_iData_type(data, 2)
        
        a_key = result['Answer']
        answer = result[a_key]
        
        self.assertEqual(answer, 'boolean')
    
    
    # checking if it creates any questions at all. 
    
    def test_generate_questions(self):
        
        data = [[0, 'def', 'function', '(',')',]
                ]
        
        questions = generate_questions(data)
        
        self.assertNotEqual(len(questions),0)
        
    
    def test_generate_questions_syntax(self):
        
        data = [[1, 'def', 'function', '(',')']]
        
        questions = generate_questions(data)
        
        syntax = False
        for x in questions:
            
            if x['id'] == 10:
                syntax = True
        self.assertEqual(syntax, True)
        
    def test_generate_questions_iData(self):
        
        data = [[0, 'x', '=', '5']]
        questions = generate_questions(data)
        idata = False
        
        for x in questions:
            
            if x['id'] == 1:
                idata = True
        self.assertEqual(idata, True)
    
    def test_generate_questions_generic(self):
        
        data = [[0, 'x', '=', '5']]
        
        questions = generate_questions(data)
        gqs = [11, 16]
        generic = False
        
        for x in questions:
            if x['id'] in gqs:
                generic = True
        self.assertEqual(generic, True)
        
    
if __name__ == '__main__':
    unittest.main()
    
    
    
    