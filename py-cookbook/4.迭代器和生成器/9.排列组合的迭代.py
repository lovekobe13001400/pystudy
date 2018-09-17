items = ['a','b','c']

from itertools import permutations,combinations,combinations_with_replacement

# for p in permutations(items):
#     print(p)
#
# #它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。 也就是说通过打乱集合中元素排列顺序生成一个元组，比如
# for p in permutations(items,2):
#     print(p)


items = ['a','b','c']
#combinations 重复的会去掉
for c in combinations(items,3):
    print(c)

#在计算组合的时候，一旦元素被选取就会从候选中剔除掉(比如如果元素’a’已经被选取了，那么接下来就不会再考虑它了)。 而函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次，比如：
for c in combinations_with_replacement(items, 3):
    print(c)

