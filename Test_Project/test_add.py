from caculator import *
from startEnd import *
class Test_add(Start_End):
    def test_add(self):
        i=Math(5,10)
        self.assertEqual(i.add(),15)
print(Test_add.__dict__)
