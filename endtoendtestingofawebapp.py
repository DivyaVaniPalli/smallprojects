from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
# open the browser
driver = webdriver.Firefox()
driver.maximize_window()
# Open the URL
driver.get("https://testautomationpractice.blogspot.com/")
# Login the form and submit the application
name = driver.find_element(By.XPATH, "//input[@id = 'name']").send_keys("Divya")
email = driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Abc@maildrop.cc")
time.sleep(5)

phone_number = driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7412589630")
address = driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("HYD")
rd_male = driver.find_element(By.XPATH, "//input[@id='male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='female']") 
rd_male.is_selected()
rd_female.is_selected()
rd_male.click()
print("select the male radio button")
rd_male.is_selected()
rd_female.is_selected()

#checkboxes
day = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id,'day')]")
print(len(day))
# select all the checkboxes
for i in range(len(day)):
    day[i].click()
# unselect all the checkboxes           
# for day in day:
#    day.click()
   
country =Select(driver.find_element(By.XPATH, "//select[@id= 'country']"))
country.select_by_visible_text("Australia")
driver.quit()