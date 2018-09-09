import heapq
class PriorityQueque:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priortity):
        # 将priority和index结合使用，在priority相同的时候比较index，pop先进入队列的元素
        #如果priortity越大，-priortity，越先弹出
        heapq.heappush(self._queue,(-priortity,self._index,item))
        self._index += 1
    #heappop() 函数总是返回”最小的”的元素，
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueque()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print(q.pop())

myque = []
heapq.heappush(myque,(3,0,'php'))
heapq.heappush(myque,(1,1,'java'))
heapq.heappush(myque,(2,2,'python'))

print(heapq.heappop(myque))#java
print(heapq.heappop(myque))#python
print(heapq.heappop(myque))#php