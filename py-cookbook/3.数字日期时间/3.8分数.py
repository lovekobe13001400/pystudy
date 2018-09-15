from fractions import Fraction

a = Fraction(5,4)
b = Fraction(7,16)

#分数计算返回分数
c = a + b #27/16
c
#分子
c.numerator
#分母
c.denominator

#分数转小数
float(c)
#限制分母，最接近的值去匹配
print(c.limit_denominator(8))
print(c.limit_denominator(2))



