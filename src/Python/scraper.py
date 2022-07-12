from selenium import webdriver
from bs4 import BeautifulSoup

# path to chromedriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# url to emulate using selenium
global_dynamicUrl = "https://www.woolworths.com.au/shop/search/products?searchTerm=beef"
# open the emulator
driver.get(global_dynamicUrl)
html = driver.page_source

# Function to get the user input
def getData():
    userChoice = input("What are you searching for? ")
    return userChoice

# Start parsing the emulated content using BeautifulSoup
soup = BeautifulSoup(html)

# Isolate the dollar prices
for tag in soup.find_all('span', class_="price-dollars"):
    print(tag.text)

# close the connection to selenium // NEEDED
driver.close()