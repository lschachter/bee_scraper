### Bee Scraper

This quick scraper uses Python's [requests](https://requests.readthedocs.io/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libraries to scrape the source code of the current day's [New York Times Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee). Spoiler alert, all the answers are in there. But this scraper is not for cheating!! (It's really not necessary for that, considering you can just look at the answers in the source code directly hehe don't do that cheating is bad :P.) This scraper simply counts the number of answers for the day, giving you a clearer idea of what you're aiming towards.

To use, make sure that both of the needed libraries are installed. You can follow along in their documentation linked above, but at the time of this writing the steps are simply

```python3
pip3 install requests
pip3 install beautifulsoup4
```

in your terminal. Enjoy!