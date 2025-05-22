import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def setup():
    firefox_options = Options()
    firefox_options.set_preference("dom.webdriver.enabled", False)

    service = Service("C:\\Users\\divyavani.palli\\Desktop\\MyVsCode\\geckodriver.exe")  # Update this path
    driver = webdriver.Firefox(service=service, options=firefox_options)

    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

    
def test_login2_and_logout(setup):
    driver = setup
    name = driver.find_element(By.XPATH, "//input[@id = 'Email']")
    name.clear()
    name.send_keys("admin@yourstore.com")
    password = driver.find_element(By.XPATH, "//input[@id = 'Password']")
    password.clear()
    password.send_keys("admin")
    login_button = driver.find_element(By.XPATH, "//button[@class = 'button-1 login-button']").click()
    assert "welcome" in driver.page_source
    logout = driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(5)
    assert "welcome" not in driver.page_source
    

