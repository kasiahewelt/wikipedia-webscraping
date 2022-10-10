import requests
from bs4 import BeautifulSoup
import pandas as pd


url_wiki = 'https://en.wikipedia.org/wiki/Netflix'
table_class = "infobox vcard"
response = requests.get(url_wiki)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
side_panel = soup.find('table', {'class': "infobox"})

df = pd.read_html(str(side_panel))
# convert list to dataframe
df = pd.DataFrame(df[0])
print(df)
