```python
import scrapy
from scrapy.crawler import CrawlerProcess
from .spiders.reddit_spider import RedditSpider
from .items import RedditScraperItem
from .pipelines import JSONExportPipeline
from .settings import SETTINGS
from .utils.remove_markup import remove_markup

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings=SETTINGS)
        self.spider = RedditSpider

    def start(self):
        self.process.crawl(self.spider)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.start()
```