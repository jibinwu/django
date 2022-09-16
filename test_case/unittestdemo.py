import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '9889d539424d324a4d'
        desired_caps['appPackage'] = 'com.qingzu.waterproof_work'
        desired_caps['appActivity'] = '.WelcomeActivity'
        desired_caps['appWaitActivity'] = '.LoginActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def test_nologin(self):
        ac = self.driver.current_activity
        self.assertEqual(ac,".LoginActivity")

    def test_success(self):
        self.driver.find_element_by_id("login_et_phone_number").send_keys("15058321650")
        self.driver.find_element_by_id("login_et_password").send_keys("123456")
        self.driver.find_element_by_id("login_bt_commit").click()
        try:
            if self.driver.find_element_by_id("login_bt_commit").is_displayed():
               exsist=False
        except Exception as e:
            exsist=True
        self.assertEqual(exsist, True)

    # def test_nologin(self):
    #     ac = self.driver.current_activity
    #     self.assertEqual(ac,".LoginActivity")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
