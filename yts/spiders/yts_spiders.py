import scrapy
from yts.items import YtsItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    p_number = 101
    start_urls = [
        'https://yts.lt/browse-movies/0/all/action/7/latest?page=31',
    ]
            
    def parse(self, response):

        items = YtsItem()
        

        for quote in response.css('div.browse-movie-wrap'):

            items['movie_name'] = quote.css('div.browse-movie-bottom a.browse-movie-title::text').get()
            items['movie_idmb'] = quote.css('h4.rating::text').get()
            items['movie_year'] = quote.css('div.browse-movie-bottom div.browse-movie-year::text').getall()[0]

            yield items
            # yield {
            #     'Title': quote.css('span.text::text').get()[1:-1],
            #     'author': quote.css('small.author::text').get(),
            #     'tags': quote.css('div.tags a.tag::text').getall(),
            # }

        next_page = 'https://yts.lt/browse-movies/0/all/action/7/latest?page='+ str(QuotesSpider.p_number)
        if QuotesSpider.p_number<=144:
            QuotesSpider.p_number+=1
            yield response.follow(next_page, callback=self.parse)
        