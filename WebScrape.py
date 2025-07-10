from bs4 import BeautifulSoup
import requests
import csv


url = 'https://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

books_data= []

for book in soup.find_all('article',class_='product_pod'):
    try:
        title = book.h3.a['title']

        price = book.find('p',class_='price_color').text


        print(f'{title} - {price}')
        print(f"price: {price}")
        print("-" * 50)

        books_data.append([title,price])

    except AttributeError as e:
        print(f"Skipping a book due to error: {e}")
        continue

with open ('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title','price'])
    writer.writerows(books_data)

print(f'\nSuccessfully saved {len(books_data)} books to books.csv')









