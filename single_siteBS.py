################################################################################
# Scraping Single Legimi
################################################################################
# This page scraps the data for one painter from wikipedia:
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
import pandas as pd
import re
from datetime import datetime

headerOne = {'User-Agent': 'Mozilla/5.0'}

books = pd.DataFrame({'title':[], 'author':[], 'publisher':[], 'category':[], 
        'language':[], 'score':[], 'ebookPrice':[], 'audiobookPrice':[], 'paperPrice':[], 'popularity':[]})

#site = 'https://www.legimi.pl/ebook-narrenturm-tom-1-andrzej-sapkowski,b458095.html'
site = 'https://www.legimi.pl/ebook-chiny-bez-makijazu-marcin-jacoby,b140079.html'
#site = 'https://www.legimi.pl/ebook-opowiadania-bizarne-olga-tokarczuk,b225553.html'

req = Request(site, headers=headerOne)

html = urlopen(req)
bs = BS(html.read(), 'html.parser')

try:
    title = bs.find('h1', {'class':'title-text'}).text #wymaga poprawki, żeby obciąć ebook i audiobook
    title = re.split(' ebook', title)[0] #save only title when ebook type
    title = re.split(' audiobook', title)[0] #save only title when audiobook type
    title = re.split(' książka papierowa', title)[0] #save only title when paperback type
except:
    title = ''

#print('This is the title: ', title)

try:
    author = bs.find('a', {'class': 'author-link'}).text
except:
    author = ''

#print('This is the author: ', author)

try:
    publisher = bs.find('a', {'class':'category-link'}).text
except:
    publisher = ''

#print('This is the publisher: ', publisher)

try:
    category = bs.find_all('a', {'class':'category-link'})[1].text
except:
    category = ''

#print('This is the category: ', category)

try:
    language = bs.find('section', {'class':'book-description'}).div.div.ul
    language = language.find_all('li')[2].span.next_sibling.text
except:
    language = ''

#print('This is the language: ', language)

try:
    score = bs.find('span', {'class':'votes-count'}).text
    score = re.findall('[0-5]{1}\,[0-9]', score)[0]
except:
    score = ''

#print('This is the score: ', score)

try:
    ebookPrice = bs.find_all('h4',string = 'ebook')[-1].parent.next_sibling.text
    ebookPrice = re.findall('[0-9]+\,[0-9]+', ebookPrice)[0]
except:
    ebookPrice = ''

#print('This is the ebook price: ', ebookPrice)

try:
    audiobookPrice = bs.find_all('h4',string = 'audiobook')[-1].parent.next_sibling.text
    audiobookPrice = re.findall('[0-9]+\,[0-9]+', audiobookPrice)[0]
except:
    audiobookPrice = ''

#print('This is the audiobook price: ', audiobookPrice)

try:
    paperPrice = bs.find_all('h4',string = 'książka papierowa')[-1].parent.next_sibling.text
    paperPrice = re.findall('[0-9]+\,[0-9]+', paperPrice)[0]
except:
    paperPrice = ''

#print('This is the paperbook price: ', paperPrice)

try:
    popularity = bs.find('p', {'class':'readers-count-text'}).text
    popularity = re.findall('[0-9]+', popularity)[0]
except:
    popularity = ''

#print('This is the popularity: ', popularity)

book = {}

book = {'title':title, 'author':author, 'publisher':publisher, 'category':category, 
        'language':language, 'score':score, 'ebookPrice':ebookPrice, 
        'audiobookPrice':audiobookPrice, 'paperPrice':paperPrice, 'popularity':popularity}


books = books.append(book, ignore_index = True)

#print(d.to_string(index=False)) #print without indexing

print(books)