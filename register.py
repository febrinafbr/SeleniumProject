import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

class DemoWebShop(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(options=option)
        self.browser.get('https://demowebshop.tricentis.com/register')
        self.assertIn("Demo Web Shop", self.browser.title)        
      
    def test_register_invalid_email(self):
        driver = self.browser
        driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Andi")
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Nian")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("andinian")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-val-email]").get_attribute('data-val-email')
        self.assertIn("Wrong email", error_message)
  
    def test_register_success(self):
        driver = self.browser
        driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Andi")
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Nian")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("andinian123@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        get_url = driver.current_url
        success_message = driver.find_element(By.CLASS_NAME, 'result').text
        self.assertIn("https://demowebshop.tricentis.com/registerresult/1", get_url)
        self.assertIn("Your registration completed", success_message)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()