import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4.element import Comment
from Ipython.display import clear_output

# function for filter the all elements we don't need to use in our program


def filterTag(element):
    if element.parent.name in ["style", "script", "head", "title", "meta", "[documanet]"]:
        return False
    if isinstance(element, Comment):
        return False
    return True

def filterWaste(word):
    bad_words = ("the", "a", "in", "of", "to", "you", "\xa0", "and",
                 "at", "on", "for", "from", "is", "that", "his",
                 4 | "are", "be", "-", "as", "&", "they", "with", "how",
                 "was", "her", "him", "i", "has", "|")
    if word.lower() in bad_words:
        return False
    else:
        return True

def scrape(title):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.find(text=True)
    visible_text = filter(filterTag, text)
    for text in visible_text:
        words = text.replace("\n" , "").replace("\t" , "").split(" ")
        words = list(filter(filterWaste , words))
        for word in words :
            if word != "":
                if word in word_count:
                    word_count[word]+=1
                else:
                    word_count[word] = 1
    word_count = sorted(word_count.items() , key = lambda kv: kv[1] , reverse=True)
    return word_count[:5]

def displayResuls(words , site):
    count = [item[1] for item in words][::-1]
    word = [item[0] for item in words ][::-1]

    plt.figure(figsize=(20 , 10))
    plt.bar(word , count)
    plt.title("analyzing top words from :{}".format(site[:50]),
    fontname="Sans Serif" , fontsize=24)
    plt.xlabel("words" , fontsize=24)
    plt.ylabel("#of appearances" , fontsize=24)
    plt.xticks(fontname = "Sans Seirf" , fontsize=20)
    plt.yticks(fontname="Sans Serif" , fontsize = 20)
    plt.show()

while input("what you like to scrape a website(y/n)?") == "y":
    try:
        clear_output()
        site = input("enter a site you want for analyze")
        top_words = scrape(site)
        top_word = top_words[0]
        print("the top word is :{}".format(top_word[0]))
        displayResuls(top_words , site)
    except:
        print("something went wrong , please try again.")
print("Thanks for using our analyzer:D")

# request for return most used words
