from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url_list = []

colesResult = {
    "name": "",
    "price": 0,
    "location": "",
    "url": ""
}

def get_url():
    url = input("Paste a URL: ")
    url_list.append(str(url))
    add_another_url()


def add_another_url():
    run_again = input("Add another URL? (y/n): ")

    if run_again == "y":
        get_url()
    elif run_again == "n":
        print("Stopping loop...")


def create_client():
    for url in url_list:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        print("Client done")
        return page_html


def scrape():
    page_soup = soup(create_client(), "html.parser")
    containers = page_soup.findAll("li", {"class" : "octopus-pc-item octopus-pc-item-v3"})

    filename = "book_info.csv"
    f = open(filename, "w")
    headers = "title, Price \n"
    f.write(headers)

    for book in containers:
        title_containers = book.find("span", {"class": "a-size-base a-color-base"})
        title = title_containers.text
        price_containers = book.find("span", {"class": "a-price"})
        price = price_containers.text.strip()
        f.write(title.replace(",", "|") + "," + price + "\n")


def main():
    get_url()
    create_client()
    scrape()


if __name__ == "__main__":
    main()