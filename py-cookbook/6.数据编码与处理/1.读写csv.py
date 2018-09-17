import csv
# with open('stocks.csv') as f:
#
#
#     f_csv = csv.reader(f)
#     #字段名
#     headers = next(f_csv)
#     print(headers)
#     for row in f_csv:
#         #l #列表
#         print(row)


#使用命名元祖
#
# from collections import namedtuple
#
# with open('stocks.csv') as f:
#     f_csv = csv.reader(f,delimiter=',')
#
#     #因为next了一下，
#     heading = next(f_csv)
#
#     #Row去了个名
#     row = namedtuple('Row',heading)
#     for r in f_csv:
#         row_one = row(*r)
#         #访问
#         print(row_one.Price)



#写

# headers = ['Symbol','Price','Date','Time','Change','Volume']
# rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
#          ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
#          ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
#        ]
#
#
# with open('write.csv','w') as f:
#
#     #先创建一个writer对象
#     f_csv = csv.writer(f)
#
#     f_csv.writeheader()
#     f_csv.writerow(rows)
#
#
#
# #字典序列
#
# headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
# rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
#         'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
#         {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
#         'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
#         {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
#         'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
#         ]
#
# with open('stocks.csv','w') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(rows)

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)