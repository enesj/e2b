```python
import re

def remove_markup(text):
    """Remove markup from the given text."""
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)
```