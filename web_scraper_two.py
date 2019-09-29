import requests
from bs4 import BeautifulSoup

url = "https://www.dailysmarty.com/topics/python"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.find_all("a")

def title_name_generator(links):
    post_titles = []
    def title_formatter(url):
        if "posts" in url:
            url = url[7:]
            url = url.replace('-', ' ')
            url = url.title()
            post_titles.append(url)
    

    for link in links:
        title_formatter(link["href"])
    
    return post_titles


post_titles = title_name_generator(links)
for post in post_titles:
    print(post)