from packages import Scraper, DBSeeder

# somewhen I want to add support for different websites

Data = Scraper.run("instant coffee")
#Data = Scraper.run(input()) 

DBSeeder.run(Data)