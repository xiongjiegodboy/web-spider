import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

url = 'https://music.163.com/discover/toplist'
response = requests.get(url=url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
all_titles = soup.find_all("ul", attrs={"class": "f-hide"})

song_list = []
for titles in all_titles:
    for title in titles.find_all("a"):
        song_list.append(title.text)

df = pd.DataFrame({'Song Title': song_list})
df.to_excel('song_list.xlsx', index=False)

# soup = BeautifulSoup(html, "html.parser")
# all_titles = soup.findAll("span", attrs={"class": "title"})
# for title in all_titles:
#     title_string = title.string
#     if "/" not in title_string:
#         print(title_string)
