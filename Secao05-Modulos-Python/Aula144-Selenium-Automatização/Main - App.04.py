"""
- Baixar o driver atual do Chrome no site https://pypi.org/project/selenium/
- Caso a conta do usuário tiver 2 etapa para logar, esse programa não vai funcionar.
- O argumento options do webdriver.Chrome(), serve pra quê? Ele usa o webdriver.ChromeOptions() que por sua
vez adiciona a pasta Perfil. Essa pasta perfil serve apenas p/ "guardar dados"? Sim, é bem interessante pra sites que
guardam dados, por exemplo, dados de login, cookies, etc...
- O selenium é para testarmos aplicações de forma automática, pois faz o mesmo que um usuário normal faria.
"""
import os

from selenium import webdriver

BASE_DIR = os.path.dirname(__file__)
PROFILE_PATH = os.path.join(BASE_DIR, 'Perfil')
DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver.exe')

driver_path = DRIVER_PATH
options = webdriver.ChromeOptions()
options.add_argument(PROFILE_PATH)
chrome = webdriver.Chrome(
    driver_path,
    options=options
)

if __name__ == '__main__':
    chrome.get('https://www.otaviomiranda.com.br/')
    posts = chrome.find_elements('post-entry')

    for post in posts:
        titulo = post.find_element_by_css_selector('h3.entry-title')
        excerto = post.find_element_by_css_selector('div.entry-content')

        print(f'Tínulo: {titulo.text}')
        print(f'Excerto: {excerto.text}')

        print('-' * 80)
