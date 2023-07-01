```python
import scrapy
from web_scraper.items import RedditScraperItem
from web_scraper.utils.remove_markup import remove_markup

class RedditSpider(scrapy.Spider):
    name = 'reddit_spider'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = RedditScraperItem()
            item['title'] = remove_markup(post.css('p.title > a::text').get())
            item['url'] = post.css('p.title > a::attr(href)').get()
            item['upvotes'] = remove_markup(post.css('div.score.unvoted::attr(title)').get())
            yield item

        next_page = response.css('span.next-button > a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```
