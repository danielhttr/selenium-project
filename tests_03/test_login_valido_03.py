import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test03:
  def test_login_valido_03(self):
    # Instancia os objetos que serão usados no teste
    login_page = LoginPage()
    home_page = HomePage()

    login_page.fazer_login("standard_user", "secret_sauce")

    home_page.verificar_login_com_sucesso()