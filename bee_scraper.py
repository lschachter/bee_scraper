from bs4 import BeautifulSoup
import requests

BEE_SITE = 'https://www.nytimes.com/puzzles/spelling-bee'

def scrape_answers(req_lib, scraper):
    '''
    A quick scraper solely to find the number of words available in the new york time's spelling bee
    game. NOT designed to display the words, just to make the end goal clearer!
    '''
    response = req_lib.get(BEE_SITE)
    scrape = scraper(response.text, 'html.parser')
    # Isolate the data we need, kept in the first js script on the page
    scrape = scrape.script.string

    answer_key = '"answers":['
    answers_index = scrape.index(answer_key) + len(answer_key)
    scrape = scrape[answers_index:]
    list_end = scrape.index(']')
    scrape = scrape[:list_end]

    scrape = scrape.replace('"', '')
    words = scrape.split(',')

    return len(words)


if __name__ == "__main__":
    print(f'There are {scrape_answers(requests, BeautifulSoup)} answers in today\'s Spelling Bee')
