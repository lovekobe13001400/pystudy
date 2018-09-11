class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    #更友好的现实，本应该是个对象，把对象可视化了
    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    #这里如果做一些额外处理，那么代理迭代就可能会有新的效果
    def add_child(self,node):
        self._children.append(node)

    #__iter__() 方法只是简单的将迭代请求传递给内部的 _children 属性。
    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    #
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)