#以深度优先方式遍历树形节点的生成器。 下面是代码示例：
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
        # self._children2 = []

    def __repr__(self):
        return "Node({!r})".format(self._value)


    def add_child(self,node):

        self._children.append(node)
        # self._children2.append(node)

    def __iter__(self):
        return iter(self._children)
    # 它首先返回自己本身并迭代每一个子节点并 通过调用子节点的 depth_first() 方法(使用 yield from 语句)返回对应元素。

    #用递归实现遍历树
    def depth_first(self):
        yield self
        #迭代self下的所有可迭代对象，猜想？？
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)



    root.add_child(child1)
    root.add_child(child2)
    # for c in root:
    #     print(c)
    # exit()
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

