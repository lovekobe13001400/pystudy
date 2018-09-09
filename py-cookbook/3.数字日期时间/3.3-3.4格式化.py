
x = 1234.56789
format(x,'0.2f')

#右对齐 8位，所以左边空2位
format(x,'>8.1f')# '  1234.6

#
format(x,'<8.2f')#'1234.57 '


format(x,',') #'1,234.56789'

format(x,'0,.2f')
format(1111111111.222,',.2f')

#指数
'''
>>> format(x, 'e')
'1.234568e+03'
>>> format(x, '0.2E')
'1.23E+03'
>>>
'''

#公式：'[<>^]?width[,]?(.digits)?'
'the value is {:0,.2f}'.format(x)


#
x = 1234
format(x,'b')
format(x,'0')
format(x,'x')