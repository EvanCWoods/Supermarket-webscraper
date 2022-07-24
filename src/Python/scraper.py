from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# path to chromedriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
chrome_options = Options()
# chrome_options.add_argument("--headless")

searchUrls = ["https://www.woolworths.com.au/shop/search/products?searchTerm=", "https://shop.coles.com.au/a/national/everything/search/"]
# Function to get the user input
def getData():
    userChoice = input("What are you searching for? ")
    return userChoice

# Function to search woolworths using the search
def searchStores():
    # Load the user choice in to memory once
    userChoice = getData()
    # url to emulate using selenium=
    for item in searchUrls:
        # open the emulator
        driver.get(item + userChoice)
        # Start parsing the emulated content using BeautifulSoup
            # second argument is for the parsing method,
                # should be looked in to
    return BeautifulSoup(driver.page_source, features="lxml")

# Isolate the dollar prices
# for tag in searchStores().find_all('span', class_="price-dollars"):
#     print(tag.text)


# Function to run the searches recursively
def getAllData():
    userChoice = getData()
    for item in searchUrls:
        driver.get(item + userChoice)
        returnPrices(BeautifulSoup(driver.page_source, features="lxml"))



# function to print the prices
def returnPrices(pageSource):
    for tag in pageSource.find_all('span', class_="price-dollars"):
        print(tag.text)




def main():
    getAllData()


if __name__=="__main__":
    main()
# # close the connection to selenium // NEEDED
# driver.close()