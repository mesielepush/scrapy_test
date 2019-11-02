import scrapy

class JokesSpider(scrapy.Spider)

name = 'jokes'
start_urls = ['http://www.laughfactory.com/jokes/family-jokes']

def parse(self, response):
    for joke in response.xpath("//div[@class='jokes']"):
        yield {
            'joke_text' : joke.xpath("//div[@class='joke-text]/p").extract_first()
        }
    next_page = response.xpath("//li[@class = 'next]/a/")