import unittest
import json
import requests

from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):

    @data(('测试-季彬武',111111),('admin','jhsc8888'))
    @unpack
    def test_getReInfo1(self,user,password):
        url = 'https://cms.mamaqunaer.com/user/login'
        content = {'loginCode': user, 'loginPassword': password}
        r = requests.post(url,data=json.dumps(content))
        self.assertEqual(r.status_code,200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
