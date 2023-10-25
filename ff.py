import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://channelmyanmar.org/'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract specific elements from the page
    # Example: Extract all links
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
