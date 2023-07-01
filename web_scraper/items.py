```python
from scrapy import Item, Field

class RedditItem(Item):
    title = Field()
    url = Field()
    author = Field()
    upvotes = Field()
    comments = Field()
    subreddit = Field()
```