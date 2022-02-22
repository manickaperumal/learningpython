from unicodedata import name
import requests
import os
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup = BeautifulSoup(response.text,"html.parser")
# heading=soup.find_all("span",class_="mw-headline")
# total_lists = soup.find(class_="mw-body-content mw-content-ltr")

data = dict()

# for head in soup.find_all("h2"):
#    if head.find("span") and head.find("span").text !="See also" and head.find("span").text != "References":
      
#       data['heading'] = head.find("span")
#       print(head.parent)



print(soup.find("h3").find("span", attrs={"id":"Acrobatic_sports"}).find_next("ul"))