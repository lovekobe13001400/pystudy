words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
#出现次数最多的3个单词
top_three = word_counts.most_common(3)
#出现次数最多的
print(top_three)
#eyes出现了几次
print(word_counts['eyes'])

#手动添加次数
#
# >>> morewords = ['why','are','you','not','looking','in','my','eyes']
# >>> for word in morewords:
# ...     word_counts[word] += 1

#或者
#ord_counts.update(morewords)