import unittest
from tutor_Parser import callSplit, is_valid, par
from tutor_Question import check_question, check_indent, create_iData_type, generate_questions

class Test_interface(unittest.TestCase):
    
    # we want to test that if tutor_Question can even create a question at all after calling the callSplit function from tutor_Parser
    def Test_interface(self):
        
        data = "# to print value of x\nprint(4)"
         
        questions = generate_questions(callSplit(data))
        
        result = False
         
        if len(questions) > 0:
             result = True
        print(result)
        self.assertEqual(result,True)
    
    # we want to see if it 
    def Test_interface_idata(self):
        
        data = "def func_one():\n    x = 15"
        
        questions = generate_questions(callSplit(data))
        result = False
        
        for x in questions:
            
            if x['id'] == 1:
                result = True
        
        self.assertTrue(result)
        
    

if __name__ == '__main__':
    unittest.main()