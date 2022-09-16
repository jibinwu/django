from caculator import *
from startEnd import *
class Test_sub(Start_End):
    def test_sub(self):
        j=Math(10,5)
        self.assertEqual(j.sub(),5)