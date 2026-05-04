from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Login Test Case
driver.get("https://example.com/login")

driver.find_element(By.ID, "email").send_keys("test@example.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login").click()

time.sleep(3)

# Dashboard Test Case
driver.get("https://example.com/dashboard")
time.sleep(3)

driver.quit()
