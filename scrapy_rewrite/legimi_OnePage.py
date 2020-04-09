#############################################
########      Legimi Single Page     ########
#############################################
import scrapy

class Booker(scrapy.Item):
    author           = scrapy.Field()
    title            = scrapy.Field()
    publisher        = scrapy.Field()
    category         = scrapy.Field()
    language         = scrapy.Field()
    score            = scrapy.Field()
    ebookPrice       = scrapy.Field()
    audiobookPrice   = scrapy.Field()
    paperPrice       = scrapy.Field()
    PeopleInterested = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'legimi_SinglePage'
    allowed_domains = ['legimi.pl/']
    start_urls = ['https://www.legimi.pl/ebook-glosy-z-zaswiatow-remigiusz-mroz,b457252.html']


    def parse(self, response):
        item = Booker()
        author_xpath           = '//a[@class="author-link author-noseparator"]/text()'
        title_xpath            = '//h1[@class="title-text"]/text()'
        publisher_xpath        = '//a[@data-reactid="117"]/text()'
        category_xpath         = '//a[@data-reactid="122"]/text()'
        language_xpath         = '//span[@data-reactid="132"]/text()'
        score_xpath            = '//span[@data-reactid="94"]/text()'
        ebookPrice_xpath       = '//p[@data-reactid="16"]/text()'
        audiobookPrice_xpath   = '//p[@data-reactid="20"]/text()'
        paperPrice_xpath       = '//p[@data-reactid="24"]/text()'
        PeopleInterested_xpath = '//div[@class="now-reading"]/p[@class="readers-count-text"]/text()'
        item['author']           = response.xpath(author_xpath).extract_first()
        item['title']            = response.xpath(title_xpath).extract_first()
        item['publisher']        = response.xpath(publisher_xpath).extract_first()
        item['category']         = response.xpath(category_xpath).extract_first()
        item['language']         = response.xpath(language_xpath).extract_first()
        item['score']            = response.xpath(score_xpath).extract_first()
        item['ebookPrice']       = response.xpath(ebookPrice_xpath).extract_first()
        item['audiobookPrice']   = response.xpath(audiobookPrice_xpath).extract_first()
        item['paperPrice']       = response.xpath(paperPrice_xpath).extract_first()
        item['title']            = response.xpath(title_xpath).extract_first()
        item['PeopleInterested'] = response.xpath(PeopleInterested_xpath).extract_first()
        yield item