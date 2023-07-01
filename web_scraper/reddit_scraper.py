```python
import scrapy
from scrapy.crawler import CrawlerProcess
from .spiders.reddit_spider import RedditSpider
from .utils.markup_remover import MarkupRemover

class RedditScraper:

    def __init__(self):
        self.process = CrawlerProcess(settings={
            'FEED_FORMAT': 'json',
            'FEED_URI': 'result.json'
        })
        self.remover = MarkupRemover()

    def start_scraping(self):
        self.process.crawl(RedditSpider)
        self.process.start() # the script will block here until the crawling is finished

    def clean_data(self):
        with open('result.json', 'r') as f:
            data = json.load(f)

        cleaned_data = self.remover.remove_markup(data)

        with open('result.json', 'w') as f:
            json.dump(cleaned_data, f)

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.start_scraping()
    scraper.clean_data()
```