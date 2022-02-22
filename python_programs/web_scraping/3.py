from unicodedata import name
import requests
import os
from bs4 import BeautifulSoup
response=requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup=BeautifulSoup(response.text,"html.parser")
heading=soup.find_all("span",class_="mw-headline")
lists=soup.find(class_="mw-headline").find_all_next("li")
# print(lists)

# for i in heading:
#  print(i.text)



for i in lists:
   print(i.a.text)
   



