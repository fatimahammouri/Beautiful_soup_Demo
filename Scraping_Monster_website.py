#  Import Requests Library
#  Import Beautiful Soup Library
#  Perform an HTTP request to the Given URL
#  Create a Python Object and Store the HTML data in the Object
#  print the content
import requests 
from bs4 import BeautifulSoup
URL = "https://www.monster.com/jobs/search/?q=Software-Engineer-&where=San-Francisco__2C-CA&intc"
page = requests.get(URL)
print (page.content)




