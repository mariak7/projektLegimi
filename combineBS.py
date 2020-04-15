from selenium import webdriver
import time
import getpass
import datetime
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
import pandas as pd
import re
from datetime import datetime

url = 'https://www.legimi.pl/ksiazki/kryminal,g212/?sort=popularity'

options = webdriver.firefox.options.Options()
options.headless = False

#not usefull when Windows user
#gecko_path = '/usr/local/bin/geckodriver'
####driver = webdriver.Firefox(options = options, executable_path = gecko_path)

driver = webdriver.Firefox(options = options)

driver.get(url)

##########################################################
#pobieranie linków ze strony sterowanej przez Selenium

#create BS object from the page source
bs = BS(driver.page_source, 'html.parser')

#w jakimś momencie trzeba pozbyć się COOKIE
button = driver.find_element_by_xpath('//i[@id="closeCookie"]').click()


maxSites = bs.find('ul', {'class':'pagination'})
maxSites = maxSites.find_all('li')[-2].text #dzięki temu dojdzie do końca strony
print(maxSites)
resultKryminal = [] #lista z linkami

#########################################################
#część z pozyskiwaniem linków i iterowaniem do maxSites

#maxSites = 1 #zmienione do testowania

for i in range(int(maxSites)):
    if(i > 0):
        button = driver.find_element_by_xpath('//a[@class="icon-arrow-right"]').click()

    time.sleep(5) #dostosować do tempa internetu, żeby strona zdążyła się załadować
    bs = BS(driver.page_source, 'html.parser')

    titles = bs.find_all('a', {'class':'book-title'}) 

    links = ['https://www.legimi.pl' + title['href'] for title in titles]
 
    for link in links:
        resultKryminal.append(link)

    print('jestem w obrocie ', i)

# Close browser:
driver.quit()

print(resultKryminal)

#Now iterate in the loop

headerOne = {'User-Agent': 'Mozilla/5.0'}

books = pd.DataFrame({'title':[], 'author':[], 'publisher':[], 'category':[], 
     'score':[], 'ebookPrice':[], 'audiobookPrice':[], 'paperPrice':[], 'peopleInterested':[]})

i = 0
for linkKryminal in resultKryminal:
    site = linkKryminal
    print('Loop for idividual sites iterator ', i)
    req = Request(site, headers=headerOne)
    try:
        html = urlopen(req)
        bs = BS(html.read(), 'html.parser')
    except:
        continue

    time.sleep(1) 
    try:
        title = bs.find('h1', {'class':'title-text'}).text #wymaga poprawki, żeby obciąć ebook i audiobook
        title = re.split(' ebook', title)[0] #save only title when ebook type
        title = re.split(' audiobook', title)[0] #save only title when audiobook type
        title = re.split(' książka papierowa', title)[0] #save only title when paperback type
    except:
        title = ''

    try:
        author = bs.find('a', {'class': 'author-link'}).text
    except:
        author = ''

    try:
        publisher = bs.find('a', {'class':'category-link'}).text
    except:
        publisher = ''

    try:
        category = bs.find_all('a', {'class':'category-link'})[1].text
    except:
        category = ''

    try:
        score = bs.find('span', {'class':'votes-count'}).text
        score = re.findall('[0-5]{1}\,[0-9]', score)[0]
    except:
        score = ''

    try:
        ebookPrice = bs.find_all('h4',string = 'ebook')[-1].parent.next_sibling.text
        ebookPrice = re.findall('[0-9]+\,[0-9]+', ebookPrice)[0]
    except:
        ebookPrice = ''

    try:
        audiobookPrice = bs.find_all('h4',string = 'audiobook')[-1].parent.next_sibling.text
        audiobookPrice = re.findall('[0-9]+\,[0-9]+', audiobookPrice)[0]
    except:
        audiobookPrice = ''

    try:
        paperPrice = bs.find_all('h4',string = 'książka papierowa')[-1].parent.next_sibling.text
        paperPrice = re.findall('[0-9]+\,[0-9]+', paperPrice)[0]
    except:
        paperPrice = ''

    try:
        peopleInterested = bs.find('p', {'class':'readers-count-text'}).text
        peopleInterested = re.findall('[0-9]+', peopleInterested)[0]
    except:
        peopleInterested = ''

    i = i+1 
    
    book = {}

    book = {'title':title, 'author':author, 'publisher':publisher, 'category':category, 
             'score':score, 'ebookPrice':ebookPrice, 
            'audiobookPrice':audiobookPrice, 'paperPrice':paperPrice, 'peopleInterested':peopleInterested}

    books = books.append(book, ignore_index = True)

    books.to_csv('kryminały_resultBS.csv') #save each time to omit problems

    #print(books)

#books.to_csv('kryminały_resultBS.csv')