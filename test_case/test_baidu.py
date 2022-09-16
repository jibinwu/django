from selenium import webdriver
from time import sleep
import unittest
class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com')

    def test_baidu(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('Selenium自学网')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        # title=self.driver.title
        self.assertEqual(self.driver.title,'Selenium自学网_百度搜索')
        self.driver.find_element_by_partial_link_text('Selenium自动化').click()
        sleep(5)
        # self.driver.find_element_by_css_selector(#kw).

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()