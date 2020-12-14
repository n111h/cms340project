import unittest
from tutor_Parser import callSplit, is_valid, par

class Test_tutor_parser(unittest.TestCase):
    
    def test_parser_with_code_block(self):                            # OK test
        arr = []
        data =  "def func_one():\n    x = 15"
        desired = [[0, 'def', 'func_one', '(', ')', ':'], [4, 'x', '=', '15']]
        lines = data.split("\n")
        for i in lines:
            if par(i) != None:
                arr.append(par(i))
        
        self.assertEqual(arr, desired)
    
    
    def test_parser_if_input_empty(self):                             # OK test
        arr = []
        data = " "
        desired = []
        lines = data.split("\n")
        for i in lines:
            if par(i) != None:
                arr.append(par(i))
        
        self.assertEqual(arr, desired)
    
    
    def test_parser_with_comment(self):                               # OK test
        arr = []
        data = "# to print value of x\nprint(4)"
        desired = [[0, 'print', '(', '4', ')']]
        lines = data.split("\n")
        for i in lines:
            if par(i) != None:
                arr.append(par(i))
        self.assertEqual(arr, desired)
        
    
    # def test_parser_with_float(self):
        
    # def test_parser_with_triple_backquote(self):
       
    def test_callSplit_empty(self):                                   # OK test
        arr = []
        data = " "

        self.assertEqual(callSplit(data), arr)
    
        
    def test_callSplit_norm_input(self):                              # OK test
        arr = []
        data =  "def func_one():\n     x = 15" 
     
        desired = [[0, 'def', 'func_one', '(', ')', ':'], [5, 'x', '=', '15']]
        self.assertEqual(callSplit(data), desired)
   
   
    def test_callSplit_ip_with_parameter(self):                       # OK test
        data = "def fun1(x)"
        
        result = callSplit(data)
        
        self.assertEqual(result,[[0,'def','fun1','(','x',')']])
        
    
    def test_is_valid_empty_input(self):                              # OK test
        data = " "
        result = is_valid(data)
        
        self.assertFalse(result)
    
    
    def test_isValid_with_triple_backquotes(self):                    # OK test
        data = "``` testing backquotes\nx = 15"
        
        result = is_valid(data)
        
        self.assertTrue(result)
        
        
if __name__ == '__main__':
    unittest.main()
        