from bs4 import BeautifulSoup
import requests

url = "https://www.dailysmarty.com/topics/python"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

posts = []
for url in soup.find_all('a'):
    all_links = url.get("href")
    if "posts" in all_links:
      posts.append(all_links)


for post in posts:
    title = post[7:]
    new_title = " ".join(title.split('-'))
    print(new_title.title())



    









