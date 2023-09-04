import unittest
from employee import Employee


class Test_employee(unittest.TestCase):
    def setUp(self):
        self.employee_1 = Employee('tom', 'smith', '20000')

    def test_name(self):
        self.assertEqual('tom', self.employee_1.first_name)

    def test_salary_rise(self):
        self.employee_1.salary_raise()
        self.assertEqual(25000, self.employee_1.salary)



