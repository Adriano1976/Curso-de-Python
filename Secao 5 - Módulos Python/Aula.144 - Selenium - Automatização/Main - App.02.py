"""
- Baixar o driver atual do Chrome no site https://pypi.org/project/selenium/
- Caso a conta do usuário tiver 2 etapa para logar, esse programa não vai funcionar.
- O argumento options do webdriver.Chrome(), serve pra quê? Ele usa o webdriver.ChromeOptions() que por sua
vez adiciona a pasta Perfil. Essa pasta perfil serve apenas p/ "guardar dados"? Sim, é bem interessante pra sites que
guardam dados, por exemplo, dados de login, cookies, etc...
- O selenium é para testarmos aplicações de forma automática, pois faz o mesmo que um usuário normal faria.
"""

import os
from time import sleep

from selenium import webdriver

BASE_DIR = os.path.dirname(__file__)
PROFILE_PATH = os.path.join(BASE_DIR, 'Perfil')
DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver.exe')


class ChromeAuto:
    def __init__(self):
        self.driver_path = DRIVER_PATH
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-data-dir={PROFILE_PATH}')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys(user_login)
            input_password.send_keys(user_password)
            sleep(3)
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    user_login = input('Login: ')
    user_password = input('Senha: ')

    chrome = ChromeAuto()
    chrome.acessa('https://github.com')

    chrome.clica_sign_in()
    chrome.faz_login()

    sleep(3)
    chrome.sair()
