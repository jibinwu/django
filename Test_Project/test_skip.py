import unittest
# @unittest.skip('skip Test1')
class Test1(unittest.TestCase):
    def setUp(self):
        print('test1 start!')
    # @unittest.skipIf(4>3,'skip testOne')
    def testOne(self):
        print('this is one')

    def testTwo(self):
        print('this is two')

    def tearDown(self):
        print('test1 end!')

class Test2(unittest.TestCase):
    def setUp(self):
        print('test2 start!')

    def testThree(self):
        print('this is three')
    @unittest.skipUnless(1>2,'skip testFour')
    def testFour(self):
        print('this is four')
    @unittest.expectedFailure
    def tearDown(self):
        print('test2 end!')

if __name__ == '__main__':
    unittest.main()


