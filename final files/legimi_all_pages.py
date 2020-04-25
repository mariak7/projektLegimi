###################################################
########      Legimi all books scraper     ########
###################################################
import scrapy
import pandas as pd
import re

#Maria responsible
class Booker(scrapy.Item):
    author           = scrapy.Field()
    title            = scrapy.Field()
    publisher        = scrapy.Field()
    category         = scrapy.Field()
    score            = scrapy.Field()
    ebookPrice       = scrapy.Field()
    audiobookPrice   = scrapy.Field()
    paperPrice       = scrapy.Field()
    PeopleInterested = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'legimi_criminal'
    allowed_domains = ['legimi.pl/']
    #extract start_urls from csv
    colnames = ['link']
    df = pd.read_csv("legimi_criminal_cat_urls.csv",names=colnames)
    links = df.link.tolist()
    start_urls = links[1:]

    def parse(self, response):
        #preparing individual book info and cleaning it
        item = Booker()
        author_xpath           = '//a[@class="author-link author-noseparator"]/text()'
        title_xpath            = '//h1[@class="title-text"]/text()'
        publisher_xpath        = '//ul[@class="list-unstyled"]/li[1]/a/text()'
        category_xpath         = '//ul[@class="list-unstyled"]/li[2]/a/text()'
        score_xpath            = '//span[@data-reactid="94"]/text()'
        ebookPrice_xpath       = '//p[@data-reactid="16"]/text()'
        audiobookPrice_xpath   = '//p[@data-reactid="20"]/text()'
        paperPrice_xpath       = '//p[@data-reactid="24"]/text()'
        peopleInterested_xpath = '//p[@class="light-text readers-count-text"]/text()'

        item['author']               = response.xpath(author_xpath).extract_first()
        item['title']                = response.xpath(title_xpath).extract_first()
        item['publisher']            = response.xpath(publisher_xpath).extract_first()
        item['category']             = response.xpath(category_xpath).extract_first()
        
        score_text                   = response.xpath(score_xpath).extract_first()
        try:
            item['score']            = re.findall('[0-5]{1}\,[0-9]', score_text)[0]
        except:
            item['score']            = ""

        ebookPrice_text              = response.xpath(ebookPrice_xpath).extract_first()
        try:
            item['ebookPrice']       = re.findall('[0-9]+\,[0-9]+', ebookPrice_text)[0]
        except:
            item['ebookPrice']       = ""

        audiobookPrice_text          = response.xpath(audiobookPrice_xpath).extract_first()
        try:
            item['audiobookPrice']   = re.findall('[0-9]+\,[0-9]+', audiobookPrice_text)[0]
        except:
            item['audiobookPrice']   = ""

        paperPrice_text              = response.xpath(paperPrice_xpath).extract_first()
        try:
            item['paperPrice']       = re.findall('[0-9]+\,[0-9]+', paperPrice_text)[0]
        except:
            item['paperPrice']       = ""

        item['title']                = response.xpath(title_xpath).extract_first()
        
        PeopleInterested_text        = response.xpath(peopleInterested_xpath).extract_first()
        try:
            item['PeopleInterested'] = re.findall('[0-9]+', PeopleInterested_text)[0]
        except:
            item['PeopleInterested'] = ""
        yield item