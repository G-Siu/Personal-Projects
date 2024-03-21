from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SITE = "https://www.fantasycritic.games/league/"
LEAGUE = "ce6cdb0b-2be1-4290-8988-1b5552b8106d/2024"

options = Options()
# Option argument to not open browser
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
# Make request using selenium
driver.get(SITE + LEAGUE)

# Assign the html to variable
html = driver.page_source
# Parse using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract body of page
page_body = soup.body

print(page_body)
