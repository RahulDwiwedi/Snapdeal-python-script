from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


username = raw_input("Enter your snapdeal username: ")
password = raw_input("Enter you snapdeal password: ")

#starting Chrome and openning login page
driver=webdriver.Chrome()
driver.get("https://www.snapdeal.com/login")

user_field = driver.find_element_by_id("userName")
user_field.send_keys(str(username))
driver.find_element_by_id("checkUser").click()

time.sleep(1)

password_field = driver.find_element_by_id('j_password_login_uc')
password_field.send_keys(password)
driver.find_element_by_id("submitLoginUC").click()

time.sleep(1)

driver.get("https://www.snapdeal.com/product/samsung-galaxy-j7-prime-32gb/5764608145562168886")

time.sleep(1)

driver.find_element_by_id("add-cart-button-id").click()
