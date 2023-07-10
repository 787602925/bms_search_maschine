import datetime

# date1 = datetime.datetime.strptime('2018-12-01 01:32:25', '%Y-%m-%d %H:%M:%S')
# date1 = datetime.datetime.strptime('03/01/2023', '%m/%d/%Y')
# date2 = datetime.datetime.strptime('03/03/2023', '%m/%d/%Y')
# print(date1 < date2)


t1 = '2 March 2023'
t2 = '10 November 2021'
t3 = '19 June 2022'
at = '6 May 2022'
adate = datetime.datetime.strptime(t3, '%d %B %Y')
# print(adate)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for dic in my_dict:
    print(dic)
