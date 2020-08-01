import unittest
from employee_functions import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.an_employee = Employee('james', 'noria', 10000)
    
    def test_give_default_raise(self):
        self.an_employee.give_raise()
        self.assertEqual(self.an_employee.annual_salary, 15000)
    
    def test_give_custom_raise(self):
        self.an_employee.give_raise(1000)
        self.assertEqual(self.an_employee.annual_salary, 11000)

unittest.main()