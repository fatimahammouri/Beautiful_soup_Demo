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


#  Create a Beautiful Soup Object --> input : HTML content we scraped 
#  Use Beautiful Soup to find a Specific Element BY using the id attribute 
#  Use find_all () to return an iterable containing all the HTML for all the job listings
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')





