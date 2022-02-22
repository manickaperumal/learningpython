import requests
import os
from bs4 import BeautifulSoup
response=requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup=BeautifulSoup(response.content,"html.parser")
heading=soup.find_all("span",class_="mw-headline")

for i in heading:
 print(i.text)


# types=soup.find_all("li",class_="mw-headline")
# for i in heading:
#  print( i.text)

# # for j in types:
# #    print(j)


