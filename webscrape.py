import requests
from bs4 import BeautifulSoup

## TO DO ##
# 
# test URL and country// SUBJECT TO CHANGE    
country = "Republic_of_Ireland"
inURL = "https://en.wikipedia.org/wiki/Politics_of_" + country


def getInfo(URL):
    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    # results = soup.find(id="mw-content-text")
    for data in soup(['style', 'script']):
        data.decompose()

    return ' '.join(soup.stripped_strings)


def sortInfo(data):
    sortedData = (data.split("Politics of", 1) [1])
    sortedData = (sortedData.split())
    return sortedData


data = sortInfo(getInfo(URL))
print(data)
f = open("test.txt", "w", encoding='utf-8')
f.write(data)
f.close

# print(page.text)