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


html = handle_http_requests('https://www.biomedcentral.com/search?searchType=publisherSearch&sort=PubDate&page=1&query=t-test+p-value')
soup = BeautifulSoup(html, 'html.parser')
a_list = soup.find_all(name='a', itemprop='citation')
url_list = ["https:" + a['href'] for a in a_list]

print(url_list)

# content = handle_http_requests(url)
# soup = BeautifulSoup(content, "html.parser")
# authors = [author.text for author in soup.find_all("span", class_='c-listing__authors-list')]
# times = [pub_time.text for pub_time in soup.find_all(attrs={"itemprop": "datePublished"})]
# links = get_all_article_links_in_a_page(url)
# url_list = [get_url_without_property(url) + a['href'].replace('/articles', '') for a in a_list]
# titles = [title.text for title in soup.find_all('a', attrs={'data-test': 'title-link'})]

