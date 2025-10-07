import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test02:
  def test_login_invalido_02(self):
    driver = conftest.driver

    # Fazendo o login no site

    driver.find_element(By.ID, "user-name").send_keys("user_standard")
    driver.find_element(By.ID, "password").send_keys("sauce_secret")
    driver.find_element(By.ID, "login-button").click()
    assert driver.find_element(By.XPATH, "//h3[@data-test='error']").is_displayed()