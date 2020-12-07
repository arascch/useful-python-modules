import requests 
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4.element import Comment
from Ipython.display import clear_output

while input("what you like to scrape a website(y/n)?")=="y":
    try:
        clear_output()
        site = input("enter a site you want for analyze")
        print(site)
    except:
        print("something went wrong , please try again.")
print("Thanks for using our analyzer:D")
