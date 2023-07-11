import tool
import main


def test_get_articles_by_date_range(start_date, end_date, keyword):
    articles = tool.get_articles_by_date_range(start_date, end_date, keyword)
    return articles


def test_search_bmc2(start_time, end_time, keyword):
    result = main.search_bmc2(start_time, end_time, keyword)
    return result


def test_search_bmc(classification, start_time, end_time, keyword):
    return main.search_bmc(classification, start_time, end_time, keyword)


# a1 = test_get_articles_by_date_range("01 July 2023", "02 July 2023", "p-value")
# print(a1)
# a2 = test_search_bmc2("01 July 2023", "02 July 2023", "p-value")
# print(a2)
a3 = test_search_bmc('Criminology-and-Criminal-Justice', "01 January 2022", "02 July 2023", "p-value")
print(a3)
