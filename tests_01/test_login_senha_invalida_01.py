from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com")

# Fazendo o login no site
driver.find_element(By.ID, "user-name").send_keys("user_standard")
driver.find_element(By.ID, "password").send_keys("sauce_secret")
driver.find_element(By.ID, "login-button").click()
assert driver.find_element(By.XPATH, "//h3[@data-test='error']").is_displayed()