import re
from dataclasses import dataclass

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

def run(data):
    # The data is a list of stuff that looks like this:
    # product(name='Gold Blend Instant Coffee (100g)', givenID='WHF620', price='3.65', store='Asda', linkAppend='/product/nescafe-gold-blend-instant-coffee/WHF620')
    # you will need to find a way to extract the data from the labling and put it into a database

    # regex string to extract the data
    # regex = r"product\(name='(.*?)', givenID='(.*?)', price='(.*?)', store='(.*?)', linkAppend='(.*?)'\)"

    pattern = re.compile(r"product\(name='[^']*', givenID='[^']*', price='[0-9]*\.[0-9]+', store='[^']*', linkAppend='[^']*'\)")
    
    for i in data:
        regexstrlst = pattern.match(data)
        print(regexstrlst)

    pass