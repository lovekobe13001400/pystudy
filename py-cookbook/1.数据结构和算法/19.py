import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry,no python')

s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))


#
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
#返回字典里面的某个内容
min_shares = min(s['shares'] for s in portfolio)
min_shares
#返回字典
min_shares = min(portfolio,key=lambda s:s['shares'])
min_shares


s = [1,2,3,4]

s2 = (x*x for x in s)
s2