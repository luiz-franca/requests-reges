import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

print(response.content)

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticia = site.find('div', attrs={'class': '_b'})
print(noticia)

# Titulo 
titulo = noticia.find('span', attrs={'class': 'bstn-h1-title'})
print(titulo.text)

# Subtitulo
subtitulo = noticia.find('span', attrs={'class': 'bstn-h1-summary'})
print(subtitulo.text)

#print(noticia.prettify())
