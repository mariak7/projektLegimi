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
#gecko_path = '/usr/local/bin/geckodriver'

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
driver = webdriver.Firefox(options = options)

# Actual program:
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

maxSites = 5
for i in range(maxSites):

    time.sleep(4) #dostosować do tempa internetu, żeby strona zdążyła się załadować
    bs = BS(driver.page_source, 'html.parser')

    titles = bs.find_all('a', {'class':'book-title'}) 

    links = ['https://www.legimi.pl' + title['href'] for title in titles]
 
    resultKryminal.append(links)

    print('jestem w obrocie ', i)

    button = driver.find_element_by_xpath('//a[@class="icon-arrow-right"]').click()

# Close browser:
driver.quit()