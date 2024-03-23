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
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    # Make request using selenium
    driver.get(OPEN_CRITIC)
    driver.set_window_size(1980, 1080)
    # Wait 2 seconds for page to load
    driver.implicitly_wait(2)

    # Accept T&C
    driver.switch_to.frame("sp_message_iframe_1084011")
    driver.find_element(By.CLASS_NAME, "sp_choice_type_11").click()
    driver.switch_to.default_content()

    # Find search bar
    search = driver.find_element(By.ID, "form1")
    search.click()
    # Type into search
    search.send_keys(released_games)

    # Look at search dropdown and check if the game exists
    text = driver.find_element(By.ID, "ngb-typeahead-0-0")
    if text.text == released_games:
        (WebDriverWait(driver, 2)
         .until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='ngb-typeahead-0-0']"))).click())
    else:
        pass

    # Screenshot the game rating
    (driver.find_element(
        By.CSS_SELECTOR,
        "div.mb-4:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
     .screenshot("screenshot.png"))


if __name__ == "__main__":
    released_games = "Dragon's Dogma 2"
    open_critic(released_games)
