##############################################
##  Legimi - all kryminal pages extraction  ##
##############################################
from selenium import webdriver
import time
import re
import pandas as pd

#function which allows me to get text from the element without using bs4 etc.
#Because we will not use bs4 in this approach even once!
def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)

gecko_path = '/home/mati_zawodowiec/Downloads/geckodriver-v0.26.0/geckodriver'
url = 'https://www.legimi.pl/katalog/kryminal,g212/?sort=popularity'
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, executable_path = gecko_path)

# List for urls
urls_list = []

#Start scraping using selenium
driver.get(url)
time.sleep(5)
button = driver.find_element_by_xpath('//i[@id="closeCookie"]').click()
time.sleep(1)

#element with last page number
last_page = driver.find_element_by_xpath('//nav/ul/li[5]/a')
max_number_page = get_text_excluding_children(driver,last_page)

#current url information
current_url_info = driver.current_url
current_link_https = re.findall(r'(https://\S+)', current_url_info)

#this loop will scrap all of the criminal books main pages
is_max_page = re.compile(r'{}'.format(max_number_page))
while True:
	next_url = driver.find_element_by_xpath(
		'//a[@class="icon-arrow-right"]')
	next_url.click()
	time.sleep(0.45)
	current_url_info = driver.current_url
	current_link_https = re.findall(r'(https://\S+)', current_url_info)
	urls_list.append(current_link_https[0])
	# print(current_link_https[0])
	if is_max_page.search(current_link_https[0]) is not None:
		break

driver.quit()

#now we can extract urls to csv file
links_df = pd.DataFrame({'link':urls_list})
#the starting url has also information about books, so we append it to the df
links_df = links_df.append({'link':url}, ignore_index=True)
links_df.to_csv('all_criminal_links.csv')