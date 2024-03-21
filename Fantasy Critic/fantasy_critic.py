from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime as dt
import time

SITE = "https://www.fantasycritic.games/league/"
LEAGUE = "ce6cdb0b-2be1-4290-8988-1b5552b8106d/2024"

options = Options()
# Option argument to not open browser
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
# Make request using selenium
driver.get(SITE + LEAGUE)

# Wait 2 seconds for page to load
time.sleep(2)

# Assign the html to variable
html = driver.page_source
# Parse using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract body of page
page_body = soup.body
# print(page_body.prettify().encode("utf-8"))

# Extract upcoming releases table
tables = page_body.select("table")[1]
# print(tables.prettify())
table_body = tables.find("tbody")
# print(table_body.prettify())

# Extract table rows
rows = table_body.find_all("tr")
# print(rows)
# Get each row name and date
for row in rows:
    columns = row.find_all("td")
    name = columns[0].text
    date = columns[1].text
    print(name, date)

# Check couple days before release
# Add name and release date to a list
# Check rating on day of release
