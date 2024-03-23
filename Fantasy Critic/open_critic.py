from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Critic
OPEN_CRITIC = "https://opencritic.com/"


def open_critic(released_games):
    options = Options()
    # Option argument to not open browser
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    # Make request using selenium
    driver.get(OPEN_CRITIC)

    # Wait 2 seconds for page to load
    driver.implicitly_wait(2)

    # Accept T&C
    # driver.switch_to.frame("sp_message_iframe_1084011")
    # driver.find_element(By.CLASS_NAME, "sp_choice_type_11").click()
    # driver.implicitly_wait(4)
    # Find search bar
    search = driver.find_element(By.ID, "form1")

    # Type into search
    search.send_keys(released_games)
    # Wait a moment for game to search
    driver.implicitly_wait(2)

    # Look at search dropdown and check if the game exists
    driver.find_element(By.ID, "ngb-typehead-0-0").click()

    # # Assign the html to variable
    # html = driver.page_source
    # # Parse using BeautifulSoup
    # soup = BeautifulSoup(html, "html.parser")


if __name__ == "__main__":
    released_games = "Dragon's Dogma 2"
    open_critic(released_games)
