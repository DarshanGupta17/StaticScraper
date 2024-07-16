import requests
from bs4 import BeautifulSoup

website = "https://subslikescript.com/movie/Avatar_The_Way_of_Water-1630029"

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content , 'lxml')

# print(soup.prettify())

box = soup.find('article',class_='main-article')

title = box.find('h1').get_text()
transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ')

with open('jobs.txt','w') as file:
    file.write(transcript)

print(title)
print(transcript)