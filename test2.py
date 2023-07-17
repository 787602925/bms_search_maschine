import re

import requests
from bs4 import BeautifulSoup
import tool


def handle_http_requests(url2):
    """
    Handle network requests
    :param url: string
    :return: response.text
    """
    response = requests.get(url2)
    content = ''
    if response.status_code == 200:
        content = response.text
    else:
        print("Failed to fetch the URL, status code:", response.status_code)
    return content


articles = tool.get_all_articles('https://biotechnologyforbiofuels.biomedcentral.com/articles?tab=keyword&searchType=journalSearch&sort=Relevance&query=t-test+p-value&page=2')
print(articles)

# content = handle_http_requests(url)
# soup = BeautifulSoup(content, "html.parser")
# authors = [author.text for author in soup.find_all("span", class_='c-listing__authors-list')]
# times = [pub_time.text for pub_time in soup.find_all(attrs={"itemprop": "datePublished"})]
# links = get_all_article_links_in_a_page(url)
# url_list = [get_url_without_property(url) + a['href'].replace('/articles', '') for a in a_list]
# titles = [title.text for title in soup.find_all('a', attrs={'data-test': 'title-link'})]

