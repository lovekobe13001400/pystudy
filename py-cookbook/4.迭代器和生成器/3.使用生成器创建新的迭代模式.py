
#

def frange(start,stop,increment):
    x = start
    while x<=stop:
        yield x
        x += increment

for i in frange(0,4,0.5):
    print(i)


#函数底层机制
def countdown(n):
    print("starting to count from",n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

c = countdown(3)

next(c)

next(c)

next(c)

#Stopiteration
next(c)