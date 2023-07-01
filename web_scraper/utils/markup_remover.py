```python
import re

class MarkupRemover:
    def __init__(self):
        self.markup_pattern = re.compile(r'<.*?>')

    def remove_markup(self, text):
        return re.sub(self.markup_pattern, '', text)
```