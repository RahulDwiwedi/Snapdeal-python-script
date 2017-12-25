from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Asking snapdeal username & password
username = raw_input("Enter your snapdeal username: ")
password = raw_input("Enter you snapdeal password: ")

# Starting Chrome and openning login page
driver=webdriver.Chrome()
driver.get("https://www.snapdeal.com/login")

# Finding userfield & filling data
user_field = driver.find_element_by_id("userName")
user_field.send_keys(str(username))
driver.find_element_by_id("checkUser").click()

# Waiting for a while
time.sleep(1)

# Finding password field & filling data
password_field = driver.find_element_by_id('j_password_login_uc')
password_field.send_keys(password)
driver.find_element_by_id("submitLoginUC").click()

# Waiting again
time.sleep(1)

# getting the product
driver.get("https://www.snapdeal.com/product/samsung-galaxy-j7-prime-32gb/5764608145562168886")

# Waiting for a while
time.sleep(1)

# adding product to cart.
driver.find_element_by_id("add-cart-button-id").click()
