from selenium import webdriver
driver=webdriver.Firefox()
driver.get('https://coding.imooc.com/class/136.html?mc_marking=60e5294c605a87b2af7257d06f70505e&mc_channel=syb7')
driver.find_element_by_css_selector('#js-signin-btn').click()
driver.find_element_by_css_selector('[name="email"]').send_keys('15058321650')
driver.find_element_by_css_selector('[name="password"]').send_keys('jbw15058321650')
driver.find_element_by_css_selector('[value="登录"]').click()

