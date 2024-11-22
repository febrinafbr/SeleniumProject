import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

class DemoWebShop(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(options=option)
        self.browser.get('https://demowebshop.tricentis.com/login')
        self.assertIn("Demo Web Shop", self.browser.title)        
      
    def test_login_invalid_email(self):
        driver = self.browser
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("andinian1234@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        error_message = driver.find_element(By.CLASS_NAME, 'validation-summary-errors').text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error_message)

    def test_login_success(self):
        driver = self.browser
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("andinian123@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        get_url = driver.current_url
        self.assertIn("https://demowebshop.tricentis.com/", get_url)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()