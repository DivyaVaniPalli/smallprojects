# Open Google Chrome using Selenium.
# Navigate to a login page (e.g., GitHub, LinkedIn).
# Enter username & password and click login.
# Take a screenshot after login.

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#  Open Google Chrome using Selenium.
driver = webdriver.Firefox()
# Navigate to a login page (e.g., GitHub, LinkedIn).
driver.get("https://admin-demo.nopcommerce.com/login")
# Enter username & password and click login.
email = driver.find_element(By.XPATH, "//input[@id = 'Email']")
email.clear()
email.send_keys("admin@yourstore.com")
password = driver.find_element(By.XPATH, "//input[@id = 'Password']")
password.clear()
password.send_keys("admin")
button = driver.find_element(By.XPATH, "//button[@class = 'button-1 login-button']").click()
# Take a screenshot after login.
folder=os.path.join(os.getcwd(),"loginpage.png")
driver.save_screenshot("C:\\Users\\divyavani.palli\\Desktop\\MyVsCode\\smallprojects\\loginpage.png")
driver.quit()