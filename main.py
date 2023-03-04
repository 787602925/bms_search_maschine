
import tool
from bs4 import BeautifulSoup

# get all classifications url from a super classification
# classification_urls = tool.get_sub_classification_urls("Chemistry")
# 472 + 312 + 163 + 8 + 70 + 760 + 411 = 2196   2205
# classification_urls = tool.get_sub_classification_urls("Criminology-and-Criminal-Justice")
# print(classification_urls)

# classification_url: http://actaneurocomms.biomedcentral.com/articles
# page: https://actaneurocomms.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=2
# for classification_url in classification_urls:
#     classification_url = classification_url + '?tab=keyword&searchType=journalSearch&sort=Relevance&query=t-test'
#     pages = tool.get_links_of_all_pages(classification_url)
#     for page in pages:
#         article = tool.get_all_article_links_in_a_page(page)
#         articles.extend(article)
#
# print(len(articles))  # 472 + 312 + 163 + 8 + 70 + 760 + 411 = 2196


def find_classification(url):
    """

    :param url: the link of the homepage
           for example: https://www.biomedcentral.com/journals
    :return: a list of classification_name: [string]
    """

    content = tool.handle_http_requests(url)
    soup = BeautifulSoup(content, "html.parser")

    if url == 'https://www.biomedcentral.com/journals':
        classification_name = [name.string for name in soup.find_all('h3')]
        classification_name.pop()
        return classification_name

    elif url == 'https://plos.org/research-communities':
        pass

    else:
        pass


def search_bmc(sort=True, classification='', lower_time=0, upper_time=0, keyword=''):
    """
    :param sort: boolean.  True --> newest first
    :param classification: string.  id of the classification. for example: "Criminology-and-Criminal-Justice"
    :param lower_time: datetime.date
    :param upper_time: datetime.date
    :param keyword: string
    :return: dict
             key: title of the article: string
             value: a list: [datetime.date, string, [string]]
                    1. Publish time: datetime.date
                    2. the url of the article: string
                    3. the author list: [string]
    """

    articles_t_test = []
    articles_keyword = []
    classification_urls = tool.get_sub_classification_urls(classification)
    # classification_url: http://actaneurocomms.biomedcentral.com/articles
    for classification_url in classification_urls:
        articles_t_test.extend(tool.search_keyword(classification_url, 't-test'))
        articles_keyword.extend(tool.search_keyword(classification_url, keyword))
        print("search for " + tool.get_url_without_property(classification_url) + " complete")
    results = tool.intersection(articles_keyword, articles_keyword)
    return results


artis = search_bmc(classification='Chemistry', keyword='t-test')
print(len(artis))
print(artis[0])
