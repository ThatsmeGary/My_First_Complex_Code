# type: ignore

import pathlib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CRIEI MINHA PRÓPRIA FUNÇÃO
def make_chrome(*options) -> webdriver.Chrome:

    chrome_options = webdriver.ChromeOptions()
    ROOT_FOLDER = pathlib.Path(__file__).parent

    CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

    for option in options:
        if option is not None:
            chrome_options.add_argument(option)
    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 15
    options = ()
    chrome_browser = make_chrome(*options)  # Abre o Chrome através da função
    chrome_browser.get('https://www.google.com')  # Abre o link desejado

    # Espera que o elemento 'q' seja localizado
    search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    # Envia uma string na parte da pesquisa
    search_input.send_keys('Python!')

    # Envia a key [ENTER]
    search_input.send_keys(Keys.ENTER)

    # Recebe os resultados de uma box de elementos
    results = chrome_browser.find_element(By.ID, 'search')

    # Recebe os links da box de elementos
    links = results.find_elements(By.TAG_NAME, 'a')

    # Clica no link 0
    links[0].click()

    # Apenas teste para baixar o PYTHON
    result = chrome_browser.find_element(By.ID, 'downloads')
    result.click()

    #       REVER

    # result = chrome_browser.find_elements(By.TAG_NAME, 'a')
    # print(result)
    # result[34].click()


time.sleep(TIME_TO_WAIT)
