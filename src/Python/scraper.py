from selenium import webdriver
from bs4 import BeautifulSoup

# path to chromedriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

# Function to get the user input
def getData():
    userChoice = input("What are you searching for? ")
    return userChoice

# Function to search woolworths using the search
def searchWoolworths():
    # url to emulate using selenium=
    searchUrl = f"https://www.woolworths.com.au/shop/search/products?searchTerm={getData()}"
    # open the emulator
    driver.get(searchUrl)
    # Start parsing the emulated content using BeautifulSoup
    return BeautifulSoup(driver.page_source)

# Isolate the dollar prices
for tag in searchWoolworths().find_all('span', class_="price-dollars"):
    print(tag.text)

# close the connection to selenium // NEEDED
driver.close()