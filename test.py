import tool
import main


def test_get_articles_by_date_range(start_date, end_date, keyword):
    articles = tool.get_articles_by_date_range(start_date, end_date, keyword)
    return articles


def test_search_bmc2(start_time, end_time, keyword):
    result = main.search_bmc2(start_time, end_time, keyword)
    return result


a1 = test_get_articles_by_date_range("01 July 2023", "02 July 2023", "p-value")
print(a1)
# a2 = test_search_bmc2("01 July 2023", "02 July 2023", "p-value")
# print(a2)
