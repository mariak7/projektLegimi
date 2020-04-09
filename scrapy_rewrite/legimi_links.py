####################################
########      Legimi A      ########
####################################
from selenium import webdriver
import scrapy
from scrapy import Selector
import time


options = webdriver.firefox.options.Options()
options.headless = False

class Link(scrapy.Item):
    link = scrapy.Field()

#class LinkListsSpider(scrapy.Spider):
#    name = 'legimi_a'
#    allowed_domains = ['legimi.pl/']
#    start_urls = ['https://www.legimi.pl/katalog/kryminal,g212/?sort=popularity']

#    def parse(self, response):
#        xpath ='//div[@class="col-xs-6 col-xssm-4 col-sm-4 col-smmd-3 col-md-20per"]/section/div/div[1]/a/@href' 
        #xpath = '//h3[//span[@id="A"]]/following-sibling::div[1]/ul/li/a[contains(translate(@href,"A","a"),"List_of_a")]/@href'
#        selection = response.xpath(xpath)
#        for s in selection:
#            l = Link()
#            l['link'] = "https://www.legimi.pl/" + s.get()
#            yield l

        #next_page = response.xpath('//*[@id="react-app"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/section/div/div[3]/div/nav/ul/li[6]/a').get()


###################################
###### Version with selenium ######
###################################

# class LinkListsSpider(scrapy.Spider):
#     name = 'legimi_a'
#     allowed_domains = ['legimi.pl/']
#     start_url = 'https://www.legimi.pl/katalog/kryminal,g212/?sort=popularity'


#     def start_requests(self):
#     	gecko_path = '/home/mati_zawodowiec/Downloads/geckodriver-v0.26.0/geckodriver'
#     	options = webdriver.firefox.options.Options()
#     	options.headless = False
#     	driver = webdriver.Firefox(options = options, executable_path = gecko_path)
#     	driver.get(self.start_url)
#     	time.sleep(5)
#     	button = driver.find_element_by_xpath('//i[@id="closeCookie"]').click()
#     	time.sleep(5)
#     	while True:
#     		next_url = driver.find_element_by_xpath(
#     			'//*[@id="react-app"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/section/div/div[3]/div/nav/ul/li[6]/a')
#     		try:
#     			self.parse(driver.page_source)
#     			next_url.click()
#     			time.sleep(5)
#     		except:
#     			break
#     	driver.close()

#     def parse(self, response):
#         xpath ='//div[@class="col-xs-6 col-xssm-4 col-sm-4 col-smmd-3 col-md-20per"]/section/div/div[1]/a/@href'
#         #xpath = '//h3[//span[@id="A"]]/following-sibling::div[1]/ul/li/a[contains(translate(@href,"A","a"),"List_of_a")]/@href'
#         selection = response.xpath(xpath)
#         for s in selection:
#             l = Link()
#             l['link'] = "https://www.legimi.pl/" + s.get()
#             yield l


######################################
###### Version V2 with selenium ######
######################################
class LinkListsSpider(scrapy.Spider):
    name = 'legimi_a'
    allowed_domains = ['legimi.pl/']
    start_urls = ['https://www.legimi.pl/katalog/kryminal,g212/?sort=popularity',
    'https://www.legimi.pl/katalog/kryminal,g212/?sort=popularity&page=2']

    def __init__(self):
    	gecko_path = '/home/mati_zawodowiec/Downloads/geckodriver-v0.26.0/geckodriver'
    	options = webdriver.firefox.options.Options()
    	options.headless = False
    	self.driver = webdriver.Firefox(options = options, executable_path = gecko_path)

    def parse(self, response):
    	self.driver.get(response.url)
    	time.sleep(5)
    	button = self.driver.find_element_by_xpath('//i[@id="closeCookie"]').click()
    	time.sleep(10)
    	while True:
    		next_url = self.driver.find_element_by_xpath(
    			'//a[@class="icon-arrow-right"]')

    		try:
    			next_url.click()
    			time.sleep(5)
    			print(self.driver.current_url)
    			xpath ='//div[@class="col-xs-6 col-xssm-4 col-sm-4 col-smmd-3 col-md-20per"]/section/div/div[1]/a/@href'
    			selection = response.xpath(xpath)
    			for s in selection:
    				l = Link()
    				l['link'] = "https://www.legimi.pl/" + s.get()
    				yield l

    		except:
    			break
    	self.driver.close()



######################################
###### Version V3 with selenium ######
######################################
# class LinkListsSpider(scrapy.Spider):
# 	name = 'legimi_a'
# 	allowed_domains = ['legimi.pl/']
# 	start_urls = ['https://www.legimi.pl/katalog/kryminal,g212/?sort=popularity']

# 	def start_requests(self):
# 		gecko_path = '/home/mati_zawodowiec/Downloads/geckodriver-v0.26.0/geckodriver'
# 		self.driver = webdriver.Firefox(options = options, executable_path = gecko_path)
# 		driver.get(self.start_urls)
# 		while True:
# 			next_url = self.driver.find_element_by_xpath(
# 				'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div/a[8]/span')
# 			try:
# 				next_url.click()
# 			except:
# 				break
# 				self.parse(driver.page_source)
# 		self.driver.close()

# 	def parse(self, response):
# 		xpath ='//div[@class="col-xs-6 col-xssm-4 col-sm-4 col-smmd-3 col-md-20per"]/section/div/div[1]/a/@href'
# 		selection = response.xpath(xpath)
# 		for s in selection:
# 			l = Link()
# 			l['link'] = "https://www.legimi.pl/" + s.get()
# 			yield l

