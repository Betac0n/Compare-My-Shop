from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
import re

dataList = list()

# This is the data class that is used to store the data so that it can be sent to DBSeeder.py to create the database seeding file(s)
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
    
    # this splits all the data into individual data points
    for storePrice in storesAndPrices.split(" "):
        storePriceSplit = storePrice.split("£")
        store = storePriceSplit[0]
        price = storePriceSplit[1]

    # Adds all the data to a data class
    global product #do you need this?
    global dataList
    dataList.append(product(linkTitle, linkGivenID, price, store, linkAppend))

def Scraper(searchItem):

    # Sanitise the search item
    searchItem = searchItem.strip().lower()
    if searchItem.find(" ") != -1:
        searchItem = searchItem.replace(" ", "-")

    # Add the search item to the URL
    URL = "https://www.trolley.co.uk/explore/" + searchItem

    # Get the webpage
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    # Check if the webpage was found
    if webpage.url == "https://www.trolley.co.uk/404/":
        print("The search item was not found, a 404 was issued")
        return

    # search HTML

    # these store ID numbers are based off what the website uses, yes I know they are missing a few numbers, I dont know why
    #stores = {"1":"asda", "2":"tesco", "3":"sainsbury's", "4":"morrisons", "6":"iceland", "7":"boots", "8":"wilko", "9":"superdrug", "10":"aldi", "11":"waitrose", "12":"b&m", "14":"savers", "15":"ocado", "16":"amazon", "18":"ebay"}
    # Currently no use for these however they may be useful in the future for doing specific searches for specific stores and their prices

    for soup_class in soup.find_all("div", class_="_stores"):
        
        #retirveing the store and price data
        pattern = re.compile(r"\+[0-9]+STORE\S?", re.IGNORECASE) #removes the +_STORES
        storesAndPrices = re.sub(pattern, '', soup_class.get_text()).rstrip()

        #handling the link and the product name
        child_soup = soup.find("a", class_="more-stores")
        linkAppend = child_soup['href']
        linkTitle = child_soup['title']
        linkGivenID = linkAppend.split("/")[3]

        # Sends found data to be compiled
        ProductDataCompiler(storesAndPrices, linkAppend, linkTitle, linkGivenID)

# This is the function that is called from the main.py to run and return stuff from this file
def run(searchItem):
    Scraper(searchItem)
    return dataList