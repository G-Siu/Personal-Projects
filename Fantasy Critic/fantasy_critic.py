from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from open_critic import open_critic
from signal import signal
import datetime as dt
import time


# Fantasy Critic league
FANTASY_CRITIC = "https://www.fantasycritic.games/league/"
LEAGUE = "ce6cdb0b-2be1-4290-8988-1b5552b8106d/2024"


def fantasy_critic_league():
    options = Options()
    # Option argument to not open browser
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    # Make request using selenium
    driver.get(FANTASY_CRITIC + LEAGUE)

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
    try:
        with open("release_soon.txt", "r") as f:
            # Read and store lines in list and emit \n
            file = f.read().splitlines()
            # Split lines into name key and date value
            games = {name: date for name, date in
                     (line.split(",") for line in file)}
    except FileNotFoundError:
        games = {}

    released = []
    # Get each row name and date
    with open("release_soon.txt", "a") as f:
        for row in rows:
            # Get columns in the row
            columns = row.find_all("td")
            # Name of game
            name = columns[0].text.strip()
            # Convert date string to datetime format
            date = dt.datetime.strptime(columns[1].text.strip(),
                                        "%Y-%m-%d").date()
            # Check if game releases within 2 days
            if dt.date.today() + dt.timedelta(days=5) >= date:
                if name not in games.keys() and date != dt.date.today():
                    # Append games to file
                    f.write(f"{name},{str(date)}\n")
            # Check release date
            if date <= dt.date.today():
                # If release today, add to list
                released.append(name)
    return released


def update_file(list_games_today):
    for game in list_games_today:
        new_lines = []
        with open("release_soon.txt", "r") as f:
            lines = f.read().splitlines()
            for line in lines:
                if game not in line and line not in new_lines:
                    new_lines.append(line)
        with open("release_soon.txt", "w") as f:
            f.write("\n".join(new_lines))
            f.write("\n")
        print(new_lines)


def main():
    released = upcoming_releases(fantasy_critic_league())
    if released:
        update_file(released)
    # Check rating on day of release
    for game in released:
        open_critic(game)
        signal()


if __name__ == "__main__":
    main()
