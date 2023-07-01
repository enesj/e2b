```python
import json
from scrapy.exceptions import DropItem
from .utils.markup_remover import MarkupRemover

class RedditScraperPipeline:
    def __init__(self):
        self.ids_seen = set()
        self.file = open('items.json', 'w')
        self.markup_remover = MarkupRemover()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            item['title'] = self.markup_remover.remove_markup(item['title'])
            item['content'] = self.markup_remover.remove_markup(item['content'])
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item

    def close_spider(self, spider):
        self.file.close()
```