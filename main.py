import requests
from bs4 import BeautifulSoup as bs

url = "http://books.toscrape.com/"

resposta = requests.get(url)

if resposta.status_code == 200:
    soup = bs(resposta.text, "html.parser")
    book_article = soup.find_all('article', attrs={'class': 'product_pod'})
    for book in book_article:
        titulo = book.h3.a['title']
        preco = book.find('p', attrs={'class': 'price_color'}).text
        link = book.h3.a['href']
        print(f"Titulo: {titulo}\nPreço: {preco}\nLink: https://books.toscrape.com/{link}")
else:
    print(resposta.status_code)