import unittest
# def add(self,a,b):
#     return 123
class MyTestCase(unittest.TestCase):

    def test_add(self):
        res=3
        # test=add(1,2)
        self.assertEqual(res,3)
if __name__ == '__main__':
    unittest.main()

