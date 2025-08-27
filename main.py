import random
from time import sleep

from src.browser import make_edge_browser

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


# from selenium.webdriver.common.keys import Keys


TIME_TO_WAIT = 120
# Example
# options = '--headless', '--disable-gpu',
# options = '--headless', '--disable-gpu',
# options = ()
options = (
    '--disable-blink-features=AutomationControlled',
    '--disable-extensions',
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-web-security',
    '--disable-features=VizDisplayCompositor',
)
browser = make_edge_browser(*options)
# browser = make_chrome_browser(*options)

browser.maximize_window()

sleep(random.uniform(1, 3))

# browser.get('https://www.nexusmods.com/games/monsterhunterwilds')
browser.get(
    'https://users.nexusmods.com/auth/sign_in?redirect_url='
    'https%3A%2F%2Fwww.nexusmods.com%2Fgames%2Fmonsterhunterwilds'
)


sleep(TIME_TO_WAIT)
sleep(TIME_TO_WAIT)
