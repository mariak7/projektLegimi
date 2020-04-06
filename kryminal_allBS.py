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
gecko_path = '/home/mati_zawodowiec/Downloads/geckodriver-v0.26.0/geckodriver'

#site = 'https://www.legimi.pl/ksiazki/kryminal,g212/?sort=popularity'
#headerOne = {'User-Agent': 'Mozilla/5.0'}

#pozyskanie wszystkich linków z podstrony używając BS

#req = Request(site, headers=headerOne)

#html = urlopen(req)
#bs = BS(html.read(), 'html.parser')

#a class book-title clampBookTitle
#titles = bs.find_all('a', {'class':'book-title'}) #wymaga poprawki, żeby obciąć ebook i audiobook
#####button = driver.find_element_by_xpath('//button[@type="submit"]')

#links = ['https://www.legimi.pl' + title['href'] for title in titles]

#for link in links:
#    print(link)


#################################

url = 'https://www.legimi.pl/ksiazki/kryminal,g212/?sort=popularity'


options = webdriver.firefox.options.Options()
options.headless = False

####driver = webdriver.Firefox(options = options, executable_path = gecko_path)
driver = webdriver.Firefox(options = options, executable_path = gecko_path)

# Actual program:
driver.get(url)



##########################################################
#pobieranie linków ze strony sterowanej przez Selenium

#create BS object from the page source
bs = BS(driver.page_source, 'html.parser')
#    tutorial_code_soup = tutorial_soup.find_all('div', attrs={'class': 'code-toolbar'})

maxSites = bs.find('ul', {'class':'pagination'})
maxSites = maxSites.find_all('li')[-2].text
print(maxSites)
resultKryminal = [] #lista z linkami

#########################################################
#część z pozyskiwaniem linków i iterowaniem do maxSites


titles = bs.find_all('a', {'class':'book-title'}) #wymaga poprawki, żeby obciąć ebook i audiobook

links = ['https://www.legimi.pl' + title['href'] for title in titles]

resultKryminal.append(links)

#for link in links:
#    print(link)


button = driver.find_element_by_xpath('//button[@type="submit"]')

#dodać iterowanie po stronach i wydobywanie linków do listy












#NIE PATRZ NA TO, SPAGHETTI

#chat = driver.find_element_by_xpath('/html/body/div[1]/div/aside[1]/div/div[1]/div[2]/ul/li[2]/button')
#chat.click()

#time.sleep(2)
#print(driver.page_source)

#bot_test_chat = driver.find_element_by_xpath('/html/body/div[1]/div/aside[2]/div[2]/div[2]/ul/li[1]/h5')
#bot_test_chat.click()

#time.sleep(2)
#print(driver.page_source)

#timestamp = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

#driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('Hello I am little bot!\n')
#time.sleep(0.3)
#driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('I messaged at: ' + timestamp + '\n')
#time.sleep(0.3)
#driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('I was run by: ' + my_email + '\n')

#time.sleep(10)
#print(driver.page_source)

# Close browser:
#driver.quit()