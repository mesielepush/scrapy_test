import scrapy
from ..items import JokeItem
from scrapy.loader import ItemLoader
class JokesSpider(scrapy.Spider):

    name = 'jokes'
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes',
                    'http://www.laughfactory.com/jokes/animal-jokes',
                    'http://www.laughfactory.com/jokes/blonde-jokes',
                    'http://www.laughfactory.com/jokes/boycott-these-jokes',
                    'http://www.laughfactory.com/jokes/clean-jokes',
                    'http://www.laughfactory.com/jokes/food-jokes',
                    'http://www.laughfactory.com/jokes/holiday-jokes',
                    'http://www.laughfactory.com/jokes/how-to-be-insulting',
                    'http://www.laughfactory.com/jokes/insult-jokes',
                    'http://www.laughfactory.com/jokes/miscellaneous-jokes',
                    'http://www.laughfactory.com/jokes/national-jokes',
                    'http://www.laughfactory.com/jokes/office-jokes',
                    'http://www.laughfactory.com/jokes/political-jokes',
                    'http://www.laughfactory.com/jokes/pop-culture-jokes',
                    'http://www.laughfactory.com/jokes/racist-jokes',
                    'http://www.laughfactory.com/jokes/relationship-jokes',
                    'http://www.laughfactory.com/jokes/religious-jokes',
                    'http://www.laughfactory.com/jokes/school-jokes',
                    'http://www.laughfactory.com/jokes/science-jokes',
                    'http://www.laughfactory.com/jokes/sex-jokes',
                    'http://www.laughfactory.com/jokes/sexist-jokes',
                    'http://www.laughfactory.com/jokes/sports-jokes',
                    'http://www.laughfactory.com/jokes/technology-jokes',
                    'http://www.laughfactory.com/jokes/word-play-jokes',
                    'http://www.laughfactory.com/jokes/yo-momma-jokes']

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            l = ItemLoader(item = JokeItem(),selector = joke)
            l.add_xpath('joke_text',".//div[@class='joke-text']/p")
            yield l.load_item()

        next_page = response.xpath("//li[@class = 'next']/a/@href").extract_first()
        print(next_page)
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback = self.parse)