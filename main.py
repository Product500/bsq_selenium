from os import getenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from dotenv import load_dotenv

load_dotenv(".env")

WEBSITE_URL = getenv("WEBSITE_URL")
SEARCH_TERMS = getenv("SEARCH_TERMS")

options = Options()
options.add_argument("--headless=new --disable-logging")


driver = webdriver.Edge(options=options)

driver.implicitly_wait(5)

driver.get(WEBSITE_URL)


search_box = driver.find_element(by=By.CLASS_NAME, value="searchTxt")

search_box.send_keys(SEARCH_TERMS)
search_box.send_keys(Keys.RETURN)

result_count = driver.find_element(by=By.CLASS_NAME, value="resultTxt")
print(f"Current URL: {driver.current_url}")
print(f"Results Found: {result_count.text}")

driver.quit()
