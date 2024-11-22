import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

class DemoWebShop(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(options=option)
        self.browser.get('https://demowebshop.tricentis.com/login')
        self.assertIn("Demo Web Shop", self.browser.title)

    def test_shopping_cart(self):
        driver = self.browser
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("andinian123@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("andi123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-item']//a[@title='Show details for $25 Virtual Gift Card']").click()
        get_url = driver.current_url
        self.assertIn("https://demowebshop.tricentis.com/25-virtual-gift-card", get_url)

        driver.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientName']").send_keys("Rani")
        driver.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientEmail']").send_keys("rani123@gmail.com")
        driver.find_element(By.XPATH, "//textarea[@id='giftcard_2_Message']").send_keys("Happy birthday!")
        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button-2']").click()
        success_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
        ).text
        self.assertIn("The product has been added to your ", success_message)
        driver.find_element(By.XPATH, "//a[normalize-space()='shopping cart']").click()
        get_url2 = driver.current_url
        self.assertIn("https://demowebshop.tricentis.com/cart", get_url2)

        driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        get_url3 = driver.current_url
        self.assertIn("https://demowebshop.tricentis.com/onepagecheckout", get_url3)

        country_dropdown = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[@id='BillingNewAddress_CountryId']"))
        )
        select = Select(country_dropdown)
        select.select_by_value("42")
        state_dropdown = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[@id='BillingNewAddress_StateProvinceId']"))
        )
        select = Select(state_dropdown)
        select.select_by_value("0")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']").send_keys("Jakarta Timur")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']").send_keys("Jalan Utara")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']").send_keys("12760")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']").send_keys("081219112589")
        continue_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@title='Continue']"))
        )
        continue_button.click()
        payment_method_next_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'button-1 payment-method-next-step-button'))
        )
        payment_method_next_button.click()
        payment_info_next_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'button-1 payment-info-next-step-button'))
        )
        payment_info_next_button.click()
        confirm_order_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'button-1 confirm-order-next-step-button'))
        )
        confirm_order_button.click()
        success_message = driver.find_element(By.XPATH, "//strong[normalize-space()='Your order has been successfully processed!']").text

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()