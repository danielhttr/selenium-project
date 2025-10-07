from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Fazendo o login no site
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Selecionando um produto (por exemplo, “Sauce Labs Backpack”) e adicionando ao carrinho
driver.find_element(By.XPATH, "//div[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.ID, "add-to-cart").click()

# Checando se o produto foi para o carrinho
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").is_displayed()

# Voltando para a página anterior e adicionando outro produto
driver.find_element(By.XPATH, "//button[@class='btn btn_secondary back btn_medium']").click()
driver.find_element(By.XPATH, "//div[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
driver.find_element(By.ID, "add-to-cart").click()

# Checando se os produtos foram para o carrinho
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
