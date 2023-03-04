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


# content = handle_http_requests('https://www.biomedcentral.com/journals')
# soup = BeautifulSoup(content, 'html.parser')
# target_li = soup.find(id='Biomedicine')
# a_list = [a['href'] for a in target_li.select('li li a:nth-of-type(1)')]
# print(a_list)
