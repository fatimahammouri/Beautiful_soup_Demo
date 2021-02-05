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


#  Create Objects for Elements with descriptive class names
#  Return only the text content of the HTML elements that the object contains
for job_elem in job_elems:

    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    #  Disregard the elements with a NONE value in them and skip over it {Advertisement} 
    if None in (title_elem, company_elem, location_elem):
        continue

    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()



