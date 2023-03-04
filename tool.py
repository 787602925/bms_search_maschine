# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import time


def handle_http_requests(url):
    """
    Handle network requests
    :param url: string
    :return: response.text
    """
    response = requests.get(url)
    content = ''
    if response.status_code == 200:
        content = response.text
    else:
        print("Failed to fetch the URL " + url + ", status code:" + str(response.status_code))
    return content


def get_sub_classification_urls(classification):
    """
    get subclassification of a super classification
    :param the id of classification: string
           for Example: 'Criminology-and-Criminal-Justice'
    :return: dic of url of articles pagination
             an element in the list: 'https://crimesciencejournal.biomedcentral.com/articles'
    """

    url = "https://www.biomedcentral.com/journals"
    content = handle_http_requests(url)
    soup = BeautifulSoup(content, "html.parser")
    target_li = soup.find(id=classification)
    a_list = target_li.select('li li a:nth-of-type(1)')
    href_list = ['http:'+a['href']+'/articles' for a in a_list]
    return href_list


def get_links_of_all_pages(url):
    """
    to get how many page of articles and return the links of all pages as a list
    :param url: a concrete link that from a classification pagination
           for Example: https://crimesciencejournal.biomedcentral.com/articles
    :return: the link list of all pages in this classification
             an element in the list: https://crimesciencejournal.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=2
    """

    url_list = []
    content = handle_http_requests(url)

    # how many pages in this concrete classification
    soup = BeautifulSoup(content, "html.parser")
    li_list = soup.find_all(name='li', class_='c-pagination__item')
    pages = int(li_list[-2].find_all(['span', 'a'])[0].text.strip())
    # modify url of all pages
    for page in range(pages):
        # url_list.append(url + '?searchType=journalSearch&sort=PubDate&page=' + str(page + 1))
        url_list.append(url + '&page=' + str(page + 1))
    return url_list


def get_all_article_links_in_a_page(url):
    """
    get all article links in a page
    :param url: the link of the page
           for example: https://crimesciencejournal.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=1
    :return: the link list of all articles in this page
    """

    content = handle_http_requests(url)
    soup = BeautifulSoup(content, 'html.parser')
    a_list = soup.find_all(name='a', itemprop='citation')
    url_list = [get_url_without_property(url) + a['href'].replace('/articles', '') for a in a_list]
    return url_list


def get_url_without_property(url):
    """
    Remove the property part of the UR
    :param url: string
    :return: url: string
    """
    return url.partition('?')[0]


def get_article_info(url):
    """
    get the article title, Publish time, authors
    :param url: the link of the article
    :return: a dictionary
    """
    content = handle_http_requests(url)
    soup = BeautifulSoup(content, "html.parser")
    author_list = [author.text for author in soup.find_all(name='a', attrs={'data-test': "author-name"})]
    dic = {'title': soup.h1.string, 'author': author_list, 'time': soup.time.string}
    return dic


def search_keyword(url, keyword):
    """
    use the search engine that comes with the page
    :param keyword: search keyword
           for example: https://actaneurocomms.biomedcentral.com/articles
    :param url: a concrete link that from a classification pagination
    :return: boolean
    """
    url = url + '?tab=keyword&searchType=journalSearch&sort=Relevance&query=' + keyword
    articles = []
    pages = get_links_of_all_pages(url)
    for page in pages:
        article = get_all_article_links_in_a_page(page)
        articles.extend(article)
    return articles


def intersection(list1, list2):
    """
    The intersection of two lists
    :param list1:
    :param list2:
    :return: res: list
    """
    res = list(set(list1) & set(list2))
    return res


# print('search for p-value start: ' + time.asctime())
# p_values = search_keyword('https://actaneurocomms.biomedcentral.com/articles', 'p-value')
# print('the number of t-test articles:' + str(len(p_values)))
# print('search for p-value end: ' + time.asctime())
# print('search for t-test start: ' + time.asctime())
# t_tests = search_keyword('https://actaneurocomms.biomedcentral.com/articles', 't-test')
# print('the number of t-test articles:' + str(len(t_tests)))
# print('search for t-test end: ' + time.asctime())
# print('the intersection start: ' + time.asctime())
# results = intersection(p_values, t_tests)
# print('the number of t-test and p-value articles: ' + str(len(results)))
# print('the intersection end: ' + time.asctime())

# t_tests = search_keyword('https://bmcimmunol.biomedcentral.com/articles', 't-test')
# print(len(t_tests))
