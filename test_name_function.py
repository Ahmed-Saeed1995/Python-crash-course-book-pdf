import unittest
from name_function import get_formatted_name
#important to let your class to inhirt from unittest to evaluate the code in exist module
class NameTestCase(unittest.TestCase):
#the test_ in the name of the function is like a way to let python know to test this code
#the function ran automatically by test_ in the start of function`s name
    def test_first_last_name(self):
        formatted_name = get_formatted_name("ahmed","hamed","saeed")
        self.assertEqual(formatted_name,"Ahmed Saeed Hamed")
    def first_last_middle_name(self):
        formatted_name = get_formatted_name("ahmed","saeed")
        self.assertEqual(formatted_name,"Ahmed Saeed")

if __name__ == '__main__':
    #run unittest to run the class automatically
    unittest.main()
