import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test03:
  def test_login_invalido_03(self):
    mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

    # Instancia os objetos que serão usados no teste
    login_page = LoginPage()

    # Faz o login
    login_page.fazer_login("user_standard", "sauce_secret")

    # Verifica se o login não foi realizado e a mensagem de erro apareceu
    login_page.verificar_mensagem_erro_login_existe()

    # Verifica o texto da mensagem de erro
    login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)
    