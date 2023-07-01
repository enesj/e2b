```python
from scrapy import Item, Field

class RedditScraperItem(Item):
    title = Field()
    url = Field()
    comments = Field()
    upvotes = Field()
    subreddit = Field()
```