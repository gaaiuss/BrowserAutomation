from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
EDGE_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_edge_browser(*options: str) -> webdriver.Edge:
    edge_options = webdriver.EdgeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    edge_service = EdgeService(
        executable_path=str(EDGE_DRIVER_EXEC),
    )

    browser = webdriver.Edge(
        service=edge_service,
        options=edge_options
    )

    return browser


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = ChromeService(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    # browser = make_edge_browser(*options)
    browser = make_chrome_browser(*options)

    browser.get('https://google.com/')

    # wait to find input
    first_name_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    first_name_input.send_keys('hello world')
    first_name_input.send_keys(Keys.ENTER)

    sleep(TIME_TO_WAIT)
