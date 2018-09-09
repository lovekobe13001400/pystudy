def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
list(dedupe(a))

#去除重复字典
def dedic(items,key=None):
    seen = set()
    for item in items:
        # print(item)#{'x': 1, 'y': 2}
        # print(key(item))#(1,2)
        # exit()
        #这里有问题：dict和list不能放进set，因为它们不可哈希
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedic(a,key=lambda d:(d['x'],d['y'])))

