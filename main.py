import datetime
import time

import tool
from bs4 import BeautifulSoup


def find_classification(url):
    """

    :param url: the link of the homepage
           for example: https://www.biomedcentral.com/journals
    :return: a list of classification_name: [string]
    """

    content = tool.handle_http_requests(url)
    soup = BeautifulSoup(content, "html.parser")

    if url == 'https://www.biomedcentral.com/journals':
        classification_name = [name.string.replace(' ', '_') for name in soup.find_all('h3')]

        classification_name.pop()
        return classification_name

    elif url == 'https://plos.org/research-communities':
        pass

    else:
        pass


def search_bmc(sort=True, classification='', lower_time='01 January 2010', upper_time=time.strftime('%d %B %Y', time.localtime()), keyword=''):
    """
    :param sort: boolean.  True --> newest first
    :param classification: string.  id of the classification. for example: "Criminology-and-Criminal-Justice"
    :param lower_time: datetime.date
    :param upper_time: datetime.date
    :param keyword: string
    :return: dict
             key: title of the article: string
             value: a dict:
                    1. 'title': string
                    2. 'publish_time': string
                    3. 'url': string
                    4. 'authors': string
    """

    articles_t_test = {}
    articles_keyword = {}
    classification_urls = tool.get_sub_classification_urls(classification)
    # classification_url: http://actaneurocomms.biomedcentral.com/articles
    for classification_url in classification_urls:
        articles_t_test.update(tool.search_keyword(classification_url, 't-test'))
        articles_keyword.update(tool.search_keyword(classification_url, keyword))
        print("search for " + tool.get_url_without_property(classification_url) + " complete")
    results1 = tool.intersection(articles_keyword, articles_t_test)
    results2 = {}
    format_lt = datetime.datetime.strptime(lower_time, '%d %B %Y')
    format_ut = datetime.datetime.strptime(upper_time, '%d %B %Y')
    for title, info in results1.items():
        format_pt = datetime.datetime.strptime(info['published_time'], '%d %B %Y')
        if format_lt <= format_pt <= format_ut:
            results2[title] = info
    return results2


def search_bmc2(start_time='01 January 2010', end_time=time.strftime('%d %B %Y', time.localtime()), keyword=''):
    """
    :param start_time: datetime.date
    :param end_time: datetime.date
    :param keyword: string
    :return: dict
             key: title of the article: string
             value: a dict:
                    1. 'title': string
                    2. 'publish_time': string
                    3. 'url': string
                    4. 'authors': string
                    5. 'pdf': string
    """
    all_articles = tool.get_articles_by_date_range(start_time, end_time, keyword)
    articles = tool.get_related_articles(all_articles, keyword)
    diagram = tool.generate_diagram(start_time, end_time, articles)
    result = tool.merge_diagram_articles(diagram, articles)
    return result
