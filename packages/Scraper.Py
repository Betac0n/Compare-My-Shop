from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
import re

# need to resort code to remove global dependencies
dataList = list()

@dataclass()
class product():

    name: str
    givenID: str #this is the ID that the website uses at the end of the URL, not quite sure what I can use it for yet but I think its important
    price: float
    store: str
    linkAppend: str #the append to https://www.trolley.co.uk that is used to get to the product page

    def __init__(self, name, givenID, price, store, linkAppend):
        self.name =  name
        self.givenID = givenID
        self.price = price
        self.store = store
        self.linkAppend = linkAppend

def ProductDataCompiler(storesAndPrices, linkAppend, linkTitle, linkGivenID):
    
    # split on £ for currency and store
    for storePrice in storesAndPrices.split(" "):
        storePriceSplit = storePrice.split("£")
        store = storePriceSplit[0]
        price = storePriceSplit[1]

    global dataList
    dataList.append(product(linkTitle, linkGivenID, price, store, linkAppend))

def Scraper(searchItem):

    searchItem = searchItem.strip().lower()
    if searchItem.find(" ") != -1:
        searchItem = searchItem.replace(" ", "-")

    URL = "https://www.trolley.co.uk/explore/" + searchItem
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    if webpage.url == "https://www.trolley.co.uk/404/":
        print("The search item was not found, a 404 was issued")
        return

    for soup_class in soup.find_all("div", class_="_stores"):
        
        pattern = re.compile(r"\+[0-9]+STORE\S?", re.IGNORECASE) #removes the +_STORES
        storesAndPrices = re.sub(pattern, '', soup_class.get_text()).rstrip()

        child_soup = soup.find("a", class_="more-stores")
        linkAppend = child_soup['href']
        linkTitle = child_soup['title']
        linkGivenID = linkAppend.split("/")[3]

        ProductDataCompiler(storesAndPrices, linkAppend, linkTitle, linkGivenID)


def run(searchItem):
    Scraper(searchItem)
    return dataList