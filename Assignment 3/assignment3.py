# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver (Make sure you have the Chrome webdriver installed and in your PATH)
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(40)
# Navigating to the Cineplex website
driver.get("https://www.wikipedia.org/")

# Waiting for the page to load
time.sleep(5)

# Click on search button
# search_button = driver.find_element("id","2")
# search_butseleniumton.click()

# Finding the search bar and entering text
# header = driver.find_elements(by=By.CLASS_NAME, value="jss13")
search_bar = driver.find_element(by=By.ID, value="searchInput")
search_bar.send_keys("selenium")
time.sleep(5)
driver.find_element(by=By.XPATH,value="/html/body/div[3]/form/fieldset/button").click()
time.sleep(5)
driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/nav/div/div/ul/li[12]/a').click()
time.sleep(5)
driver.find_element(by=By.LINK_TEXT,value="Talk").click()
time.sleep(5)
driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/div[2]/nav/div[1]/div/ul/li[2]/a').click()

time.sleep(10)