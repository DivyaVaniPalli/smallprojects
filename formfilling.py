from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://way2automation.com/way2auto_jquery/")
name = driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Divya")
email = driver.find_element(By.XPATH, "//input[@name='email']").send_keys("abc@maildrop.cc")
telphone= driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("7896541233")
country =Select(driver.find_element(By.NAME, "country"))
country.select_by_visible_text("Angola")
city = driver.find_element(By.XPATH, "//input[@name='city']").send_keys("hyd")
username= driver.find_element(By.XPATH, "//div[@id='load_box']//input[@name='username']").send_keys("ABC")
password = driver.find_element(By.XPATH, "//div[@id='load_box']//input[@name='password']").send_keys("Abc@123")
submit = driver.find_element(By.XPATH, "//div[@id='load_box']//input[@value='Submit']").click()
folder=os.path.join(os.getcwd(),"submit.png")
driver.save_full_page_screenshot("C:\\Users\\divyavani.palli\\Desktop\\MyVsCode\\smallprojects\\loginpage.png")