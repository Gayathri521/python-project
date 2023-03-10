import unittest
import HtmlTestRunner
from testing_programs import programnumber1
class My_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(programnumber1.add_two_numbers(10,20),30)
    def test_case2(self):
        self.assertEqual(programnumber1.add_two_numbers(-10,20),10)
    def test_case3(self):
        self.assertEqual(programnumber1.add_two_numbers(-10,-20),-30)
    def test_case4(self):
        self.assertEqual(programnumber1.add_two_numbers(10,-20), -10)
test_suite=unittest.TestSuite()
test_suite.addTest(My_test("test_case1"))
# test_suite.addTest("test1")
testRunner=HtmlTestRunner.HTMLTestRunner(output='reports')
testRunner.run(test_suite)

