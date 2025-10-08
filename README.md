🧪 Selenium com Python — Evolução de Automação de Testes

Este repositório documenta minha jornada de aprendizado em automação de testes com Selenium e Python, partindo de scripts básicos até a implementação de uma estrutura profissional utilizando o Page Object Model (POM) e Pytest.

🚀 Objetivo do Projeto

O objetivo é demonstrar, de forma progressiva, como construir testes automatizados para aplicações web, evoluindo a estrutura de código e boas práticas a cada etapa.

A aplicação utilizada para os testes é o site Sauce Demo, um ambiente voltado para aprendizado e prática de automação.

⚙️ Tecnologias Utilizadas
Python 3.10+, Selenium WebDriver, Pytest, webdriver-manager, chromedriver-binary

🧱 Conceitos Aplicados
Uso do Page Object Model (POM) para desacoplar lógica de teste e mapeamento de elementos.
Aplicação de fixtures do Pytest para controle de setup e teardown.
Implementação de esperas explícitas e interações avançadas (duplo clique, teclas, etc.).
Escrita de assertivas legíveis e descritivas para validação de cenários.

▶️ Como Executar os Testes

Clone o repositório

git clone https://github.com/seu-usuario/selenium-python-course.git
cd selenium-python-course


Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


Instale as dependências

pip install -r requirements.txt


Execute os testes

Testes da primeira fase:
python tests_01/test_login_valido.py

Testes com Pytest:
pytest -v -s tests_02/

Testes com Page Object Model:
pytest -v -s tests_03/
