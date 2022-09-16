import unittestdemo
import unittest
mysuite=unittest.TestSuite()
mysuite.addTest(unittestdemo.MyTestCase('test_nologin'))
mysuite.addTest(unittestdemo.MyTestCase('test_success'))
myrunner=unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)

# mysuite=unittest.TestLoader().loadTestsFromTestCase(unittestdemo.MyTestCase)
# unittest.TextTestRunner(verbosity=2).run(mysuite)