################################################################
########      Legimi criminal books urls extraction     ########
################################################################
import scrapy
import pandas as pd 

class Link(scrapy.Item):
	link = scrapy.Field()

#Mateusz responsible
class LinkListsSpider(scrapy.Spider):
	name = 'legimi_criminal_cat_urls'
	allowed_domains = ['legimi.pl/']
	
	#extract start_urls from csv
	colnames = ['year', 'link']
	df = pd.read_csv("all_criminal_links.csv",names=colnames)
	links = df.link.tolist()
	start_urls = links[1:]

	def parse(self, response):
		xpath ='//div[@class="col-xs-6 col-xssm-4 col-sm-4 col-smmd-3 col-md-20per"]/section/div/div[1]/a/@href' 
		selection = response.xpath(xpath)
		for s in selection:
			l = Link()
			l['link'] = "https://www.legimi.pl/" + s.get()
			yield l