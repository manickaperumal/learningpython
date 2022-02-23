
import requests
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

# def smallheading(x):
# text=(soup.find("h3"))
# attr=text.find("span")

# print(attr["id"])

def topic(x):

    for small_head in soup.find_all("h3"):
        if small_head.find("span",attrs={"id":x}):
            heading=small_head.text
            sub=small_head.find_next("ul")
            print(heading)
            
            print(sub.text)


topic("Air_sports")
topic("Archery")
























# def smallheading(x):

# # text=(soup.find("h3").find("span", attrs={"id":x}).find_next("ul"))
# # print(text.text)




# smallheading("Acrobatic_sports")
# smallheading("Air_sports")
# smallheading("Ball-over-net_games")

# text=(soup.find("h3").find("span", attrs={"id":"Acrobatic_sports"}).find_next("ul"))
# print(text.text)
