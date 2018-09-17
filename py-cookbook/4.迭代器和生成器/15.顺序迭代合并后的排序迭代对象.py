import heapq

a = [5,4,7,10]
b = [2,5,6,11,1]

for c in heapq.merge(a,b):
    print(c)
#好像是2,5,4,5每对排序
#1 2 4 5 6 7 10 11

