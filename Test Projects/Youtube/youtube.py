import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up your Selenium driver (replace with your actual driver path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to YouTube
driver.get('https://www.youtube.com/')

# Pause for 3 seconds
time.sleep(3)

# Wait for the page to load (adjust timeout if needed)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search-input")))

# Wait for 3 seconds
time.sleep(3)

# Find the search box and type "pictures of spiderman"
search_box = driver.find_element(By.ID, "search-input")
search_box.send_keys("pictures of spiderman")

# Find the search button and click it
search_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Search')]")
search_button.click()

# Keep the browser open for a while to view the results (optional)
time.sleep(10)

# Close the browser
# driver.quit()