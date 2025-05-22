import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver=webdriver.Firefox()
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_login(setup):
    driver=setup
    name = driver.find_element(By.XPATH, "//input[@id = 'Email']")
    name.clear()
    name.send_keys("admin@yourstore.com")
    password = driver.find_element(By.XPATH, "//input[@id = 'Password']")
    password.clear()
    password.send_keys("admin")
    login_button = driver.find_element(By.XPATH, "//button[@class = 'button-1 login-button']").click()
    
    
    