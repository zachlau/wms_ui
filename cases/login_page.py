import unittest, time
from selenium import webdriver

class Login_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://123.56.99.53:8080/WMS")

    def test_login_01(self):
        '''用户名、密码正确'''
        driver = self.driver
        driver.find_element_by_id("userID").send_keys("1001")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("checkCode").send_keys("6666")
        driver.find_element_by_id("submit").click()
        time.sleep(1)
        driver.get("http://123.56.99.53:8080/WMS/mainPage")
        time.sleep(3)

    def test_login_02(self):
        '''密码错误'''
        driver = self.driver
        driver.find_element_by_id("userID").send_keys("1001")
        driver.find_element_by_id("password").send_keys("000000")
        driver.find_element_by_id("checkCode").send_keys("6666")
        driver.find_element_by_id("submit").click()
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.quit()