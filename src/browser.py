from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from src.variables import CHROME_DRIVER_PATH, EDGE_DRIVER_EXEC


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
