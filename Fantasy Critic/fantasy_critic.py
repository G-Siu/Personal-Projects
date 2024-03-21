from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime as dt
import time

SITE = "https://www.fantasycritic.games/league/"
LEAGUE = "ce6cdb0b-2be1-4290-8988-1b5552b8106d/2024"


def fantasy_critic_league():
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
    return soup.body
    # print(page_body.prettify().encode("utf-8"))


def upcoming_releases(page_body):
    # Extract upcoming releases table
    tables = page_body.select("table")[1]
    # print(tables.prettify())
    table_body = tables.find("tbody")
    # print(table_body.prettify())

    # Extract table rows
    rows = table_body.find_all("tr")
    # print(rows)

    # Check local if already saved game recently
    with open("release_soon.txt", "r") as f:
        # Read and store lines in list and emit \n
        file = f.read().splitlines()

    # Split lines into name key and date value
    games = {name: date for name, date in (line.split(",") for line in file)}

    # Get each row name and date
    for row in rows:
        # Get columns in the row
        columns = row.find_all("td")
        # Name of game
        name = columns[0].text.strip()
        # Convert date string to datetime format
        date = dt.datetime.strptime(columns[1].text.strip(),
                                    "%Y-%m-%d").date()
        # Add new games to dictionary
        games[name] = str(date)

    # for name, date in games:
    #     # Check if game releases within 2 days
    #     if dt.date.today() + dt.timedelta(days=2) >= date:
    #         # Append games to file
    #         with open("release_soon.txt", "a") as f:
    #             f.write(f"{name},{str(date)}\n")


def main():
    upcoming_releases(fantasy_critic_league())
# Check couple days before release
# Add name and release date to a list
# Check rating on day of release


if __name__ == "__main__":
    main()
