# subscriptions/utils.py
from bs4 import BeautifulSoup
import requests

def get_top_article():
    response = requests.get("https://news.ycombinator.com/news")
    yc_page = response.text
    soup = BeautifulSoup(yc_page, 'html.parser')
    
    articles = soup.find_all(name='span', class_='titleline')
    article_scores = soup.find_all(name='span', class_='score')
    
    all_articles = [article.getText() for article in articles]
    all_links = [article.find('a').get("href") for article in articles]
    all_votes = [int(score.getText().split()[0]) for score in article_scores]

    highest_index = all_votes.index(max(all_votes))
    
    return all_articles[highest_index], all_links[highest_index]
