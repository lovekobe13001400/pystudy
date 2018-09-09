#

text = 'hello world'
#左对齐(填充)
text.ljust(20,'=')
#右对齐
text.rjust(20)

#中间对齐
text.center(20,'*')

#format也能做对齐操作,格式化操作


format(text, '>20')
format(text, '<20')
#填充放最左边
format(text, '+^20')