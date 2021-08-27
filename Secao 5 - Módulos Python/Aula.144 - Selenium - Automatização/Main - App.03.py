"""
-  Tem um método que chama, "wait", que você pode esperar por algo na tela por alguns segundos, só que ele
levanta uma exceção caso não encontre o elemento.
"""
import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = os.path.dirname(__file__)
PROFILE_PATH = os.path.join(BASE_DIR, 'Perfil')
DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver.exe')


class ChromeAuto:
    def __init__(self):
        self.driver_path = DRIVER_PATH
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-data-dir={PROFILE_PATH}')
        self.options.add_argument('window-size=1280,720')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def comeca(self) -> None:
        try:
            # Aqui, o programa espera 10 segundos até.
            element = WebDriverWait(self.chrome, 10).until(
                # Aqui encontra o elemento.
                EC.presence_of_element_located(
                    # <body> por nome (TAG_NAME)
                    (By.TAG_NAME, 'body')
                )
            )

            # Mostra o HTML do GOOGLE
            # print(element.get_attribute('innerHTML'))

            self.chrome.quit()
        except TimeoutException:
            self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa(
        'https://www.google.com.br/'
    )
    chrome.comeca()
