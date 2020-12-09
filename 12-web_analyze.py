import requests 
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4.element import Comment
from Ipython.display import clear_output

#function for filter the all elements we don't need to use in our program
def filterTag(element):
    if element.parent.name in ["style" , "script" , "head" , "title" , "meta" , "[documanet]"]:
        return False
    if isinstance(element , Comment):
        return False
    return True 

def scrape(title):
    page = requests.get(site)
    soup = BeautifulSoup(page.content , "html.parser")
    text = soup.find(text=True)
    visible_text = filter(filterTag , text)


while input("what you like to scrape a website(y/n)?")=="y":
    try:
        clear_output()
        site = input("enter a site you want for analyze")
        scrape(site)
    except:
        print("something went wrong , please try again.")
print("Thanks for using our analyzer:D")

#request for return most used words 

