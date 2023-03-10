import unittest
from testing1  import employee salary
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employeesalary( 'Rahul',50000)
    def test_email(self):
        self.assertEqual(self.employeesalary.email,'rahul@example.com')
    def test_apply_raise(self):
        self.employee.apply_raise(10)
        self.assertEqual(self.employee.salary,55000)
if __name__ == '__main__':
    unittest.main()
