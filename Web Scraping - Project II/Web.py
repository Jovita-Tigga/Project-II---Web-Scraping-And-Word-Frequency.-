# WEB SCRAPING FROM https://discoverpoetry.com/poems/100-most-famous-poems/

# Import Libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://discoverpoetry.com/poems/100-most-famous-poems/"

# Send a GET request to the website and store the response object
response = requests.get(url)
html = response.content

# Check if the response status code is 200 (OK)
if response.status_code == 200:

# Parse the response content as HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

# Find the title element using its tag name
    title = soup.find("title").text
   
# Find the  paragraph element using its tag name
    paragraphs = soup.find_all("p")

# Print the text content of the title and the paragraph
    print(soup.prettify())
    print(title)
    print(paragraphs) 
else:
# Print an error message if the response status code is not 200
    print("Error: Unable to access the website")

# Create a text file to store the scraped data
with open("Data.txt", "w") as file:
    file.write(str(paragraphs))

# Close the file
file.close()
