from dataclasses import dataclass

# I'm unsure as to wether I should handle the data class exclusivly here or not
# currently thinking about a way to simplify the process of adding new products, however unsure about how to approach
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

def pullData(data):

    dataList = list()

    for i in data:
        product = i
        dataList.append(product)

    return dataList

def run(data):
    
    dataList = pullData(data)


    return # return the seeder file to Main