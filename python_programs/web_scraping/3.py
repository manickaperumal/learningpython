import requests
from bs4 import BeautifulSoup
response=requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup=BeautifulSoup(response.content,"html.parser")
heading=soup.find(class_="mw-headline")
print(heading.text)