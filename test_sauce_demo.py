from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 


class TestSauceDemo:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()


    def test_invalid_user(self):
        self.driver.find_element(By.ID,"user-name").send_keys("")
        self.driver.find_element(By.ID,"password").send_keys("")
        self.driver.find_element(By.ID,"login-button").click()
        error_message_user = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = error_message_user.text == "Epic sadface: Username is required"
        print(f"Test Sonucu: {testResult}")
        sleep(3)


    def test_invalid_password(self):
        self.driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID,"password").send_keys("")
        self.driver.find_element(By.ID,"login-button").click()
        error_message_password = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = error_message_password.text == "Epic sadface: Password is required"
        print(f"Test Sonucu: {testResult}")
        sleep(3)


    def test_invalid_lock(self):
        self.driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        error_message_lock = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = error_message_lock.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {testResult}")
        sleep(3)


    def test_valid_item(self):
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        list_of_courses = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = len(list_of_courses) == 6
        print(f"Test Sonucu: {testResult}")
        sleep(3)


    def test_invalid_match(self):
        wait = WebDriverWait(self.driver,5).until
        wait(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        wait(ec.visibility_of_element_located((By.ID,"password"))).send_keys("1")
        self.driver.find_element(By.ID,"login-button").click()
        error_message_match = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = error_message_match.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        sleep(3)


    def test_add_product(self):
        wait = WebDriverWait(self.driver,5).until
        wait(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        wait(ec.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        add_to_cart = wait(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")))
        add_to_cart.click()
        shopping_cart_link = wait(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        shopping_cart_link.click()
        product =wait(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']")))
        message_product= product.text
        print(f"Sepetteki urun adı: {message_product}")
        continue_shopping = wait(ec.visibility_of_element_located((By.XPATH,"//*[@id='continue-shopping']")))
        continue_shopping.click()
        remove = wait(ec.visibility_of_element_located((By.XPATH,"//*//*[@id='remove-sauce-labs-backpack']")))
        remove.click()  
        sleep(3)     



    def test_product_review(self):
        wait = WebDriverWait(self.driver,5).until
        wait(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        wait(ec.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.execute_script("window.scrollTo(0,500)")
        item_name = self.driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
        item_text= item_name.text
        item_name.click()
        print(f"Ürün Başlığı: {item_text}")
        product_title = self.driver.find_element(By.XPATH,"//*[@id='inventory_item_container']/div/div/div[2]/div[1]")
        product_text =product_title.text
        print(f"Ürün Tanımı: {product_text}")
        testResult = item_text == product_text
        print(f"Ürünler aynı: {testResult}")
        backButton = self.driver.find_element(By.XPATH,"//*[@id='back-to-products']")
        backButton.click()
        sleep(5)


testClass = TestSauceDemo()
#testClass.test_invalid_user()    
#testClass.test_invalid_password()    
#testClass.test_invalid_lock()
#testClass.test_valid_item()
#testClass.test_invalid_match()
#testClass.test_add_product()
testClass.test_product_review()