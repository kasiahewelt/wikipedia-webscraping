import requests
from bs4 import BeautifulSoup
import wikipedia
import pandas as pd

companies = pd.read_csv("companies.csv")

companies_list = companies['company'].values.tolist()

for company in companies_list:
    word = company.replace(' ', '_')
    url_wiki = 'https://en.wikipedia.org/wiki/'+word
    table_class = "infobox vcard"
    response = requests.get(url_wiki)

    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    side_panel = soup.find('table', {'class': "infobox"})

    df = pd.read_html(str(side_panel))
    # convert list to dataframe
    df = pd.DataFrame(df[0])
    df['company'] = company
    print(df)
