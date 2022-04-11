from bs4 import BeautifulSoup
import requests
import pandas as pd

contact_info = []
roomLinks = []


def kamernetNlRooms():

    url = "https://kamernet.nl/huren/kamers-nederland?pageno=1"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")
    df = soup.find(class_="search-results-pagination")
    ul = df.find(class_="pagination")
    li = ul.find_all(class_="waves-effect")
    count = int(li[-2].text)

    for i in range(1, count):

        url = "https://kamernet.nl/huren/kamers-nederland?pageno=" + str(i)
        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")

        list_items = soup.find_all(class_="rowSearchResultRoom")

        for item in list_items:
            roomLinks.append(item.a["href"])

    writeOnFile(roomLinks, "roomLinkFile")


def writeOnFile(link_list, fileName):
    df = pd.DataFrame(link_list)
    df.to_csv(fileName + '.ftr', index=False, header=False)


url = "https://kamernet.nl/huren/kamers-nederland?pageno=1"
result = requests.get(url)
soup = BeautifulSoup(result.content, "html.parser")
df = soup.find(class_="search-results-pagination")
ul = df.find(class_="pagination")
li = ul.find_all(class_="waves-effect")
count = int(li[-2].text)

print(ul)