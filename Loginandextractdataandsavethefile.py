from selenium import webdriver
from selenium.webdriver.common.by import By

#  Launch Browser & Open a Website
driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

#enter the username and password automatically.
email = driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Abc@maildrop.cc")
password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Divya@7410")
sign_in = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']").click()

driver.implicitly_wait(5)