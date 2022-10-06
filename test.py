import requests
import string
from bs4 import BeautifulSoup

Enter_input = input("Search: ")
u_i = string.capwords(Enter_input)
lists = u_i.split()
word = "_".join(lists)

url = "https://en.wikipedia.org/wiki/"+word


def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details = soup('table', {'class': 'infobox'})
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x, y in zip(heading, detail):
                    print("{} :: {}".format(x.text, y.text))
                    print("----------------------------")
    for i in range(1, 3):
        print(soup('p')[i].text)
