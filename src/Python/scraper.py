from bs4 import BeautifulSoup
import requests
import re

section = "https://shop.coles.com.au/a/national/triple-flybuys-points-selection/browse/meat-seafood/beef-veal?pageNumber=1"

def getHTMLdocument(url):    
    # request for HTML document of given url
    response = requests.get(url)
    # response will be provided in JSON format
    return response.text


def runScrape():
    html_document = getHTMLdocument(section)
    # create soap object
    soup = BeautifulSoup(html_document, 'html.parser')
    for a in soup.find_all("a"):
        print(a.href)
    print(soup)


def main():
    runScrape()

if __name__=="__main__":
    main()