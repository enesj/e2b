1. Scrapy: All the files share the Scrapy library as a dependency. Scrapy is a Python framework for large scale web scraping. It provides all the tools needed to extract data from websites, process it, and store it in your preferred format.

2. RedditScraperItem: This is a data schema defined in "items.py" and used in "reddit_scraper.py" and "reddit_spider.py" to structure the scraped data.

3. RedditSpider: This is a Scrapy Spider defined in "reddit_spider.py". It is used in "reddit_scraper.py" to start the scraping process.

4. JsonWriterPipeline: This is a Scrapy Pipeline defined in "pipelines.py". It is used in "settings.py" to specify how the scraped data should be processed and stored.

5. SETTINGS: This is a dictionary defined in "settings.py" that contains configuration for the Scrapy project. It is used in "reddit_scraper.py" to configure the Scrapy spider.

6. DOM Elements: The specific DOM elements to be scraped are defined in "reddit_spider.py". These would include the id names of the elements containing the data to be scraped from Reddit.

7. Output File: "output.json" is the file where the scraped data is stored. This filename is used in "pipelines.py" to specify where the JsonWriterPipeline should write the data.

8. start_requests, parse, and parse_page: These are function names used in "reddit_spider.py" for initiating the request to Reddit, parsing the response, and handling pagination respectively. 

9. process_item: This is a function name used in "pipelines.py" to process each item scraped by the spider.