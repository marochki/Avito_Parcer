import requests
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/user/reviews/i120860146'  # замените 'xxxxx' на идентификатор аккаунта
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
reviews = soup.find_all('div', class_='reviews-reviews-text')
for review in reviews:
    print(review.text)
with open('reviews.txt', 'w', encoding='utf-8') as file:
    for review in reviews:
        file.write(review.text + '\n')
