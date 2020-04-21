#############################################
########      Legimi Single Page     ########
#############################################
import scrapy
import pandas as pd

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

        item['author']           = response.xpath(author_xpath).extract_first()
        item['title']            = response.xpath(title_xpath).extract_first()
        item['publisher']        = response.xpath(publisher_xpath).extract_first()
        item['category']         = response.xpath(category_xpath).extract_first()
        item['score']            = response.xpath(score_xpath).extract_first()
        item['ebookPrice']       = response.xpath(ebookPrice_xpath).extract_first()
        item['audiobookPrice']   = response.xpath(audiobookPrice_xpath).extract_first()
        item['paperPrice']       = response.xpath(paperPrice_xpath).extract_first()
        item['title']            = response.xpath(title_xpath).extract_first()
        item['PeopleInterested'] = response.xpath(peopleInterested_xpath).extract_first()
        yield item