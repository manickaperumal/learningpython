
import requests
import os
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/List_of_sports")
soup = BeautifulSoup(response.text,"html.parser")
# heading=soup.find_all("span",class_="mw-headline")
# total_lists = soup.find(class_="mw-body-content mw-content-ltr")

data = dict()
d = list()
for head in soup.find_all("h2"):
   if head.find("span") and head.find("span").text !="See also" and head.find("span").text != "References":
      
      data['heading'] = head.find("span")
      d.append(data['heading']['id'])
    #   print(head.parent)

      print(data)


# def topic(x):
#     list=[]
#     for small_head in soup.find_all("h3"):
#         if small_head.find("span",attrs={"id":x}):
#             # print(small_head)
#             heading=small_head.text
          
#             sub=small_head.find_next("ul")
#             # print(sub.text)
            
#             list.append(sub.text)
#             for i in list:
#                 j=i
#             l1=j.split("\n")
#             print(l1)
           
#             # print(sub)
#             # for i in sub:
#             #     list.append(i.text)
#             # print(heading)
#             path="/home/manikam"
#             os.mkdir("/home/manikam/physical/{}".format(heading))
#             file_write_path="/home/manikam/physical/{}".format(heading)
#             print(file_write_path)


#             for root,dir,file in os.walk(path):
#                 for i in dir:
                    
#                     #  print (i)
#                      if i==heading:
#                         for li in l1: 

#                          with open ("/home/manikam/physical/{0}/{1}".format(heading,li),"w")as f:
#                                 small_url="https://en.wikipedia.org/wiki/List_of_sports/" + str(heading)
#                                 res=requests.get(small_url)
#                                 soup1=BeautifulSoup(res.content,"html.parser")
#                                 i=soup1.find("table",class_="infobox vevent")
#                                 j= i.find_next("p")
#                                 f.write(j.text)

                        
           
# topic("Air_sports")
#                                 # print(list)
# # topic("Archery")
# # topic("Climbing")
# # topic("Cycling")
# # topic("Catching_games")