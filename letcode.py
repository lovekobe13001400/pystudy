
#节点类
class Node(object):
    def __init__(self,data,nNext = None):
        self.data = data
        self.next = nNext
#链表类
class Chain(object):
    def __init__(self):
        self.head = None
        self.length = 0

    #只加一个节点
    def append(self,dataOrNode):
        #item得是一个Node,加的如果只是一个数，得变成Node
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        #头为空
        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            #找到最后一个点把它连起来
            while node.next:
                node = node.next
            #如果item是一个链子如何解决
            node.next = item
            self.length += 1
    #删除一个节点
    def delete(self,index):
        if index<0 or index>=self.length:
            return None

        current = self.head
        pre    = None
        temp_index = 0
        while current.next:
            if temp_index == index:
                if not pre:
                    self.head = current.next
                else:
                    pre.next = current.next
                self.length -= 1
                return
            pre = current
            current = current.next
            temp_index += 1
    #链表反转
    def reverse(self,head):
        cur = head
        pre = None
        while cur is not None:
            #print(head)
            tmp = cur.next
            cur.next = pre
            pre = cur
            #print(pre.data)
            cur = tmp
        head = pre

    def tt(self,head):
        print(id(head))
        head = {'b':2}

def tt(head):
    head['b'] = 2
    #head = {'b':2}

mychain = Chain()
mychain.head = {'a':1}
print(id(mychain.head))
mychain.tt(mychain.head)
print(id(mychain.head))
print('-----------')
head = {'a':1}
tt(head)
print(head)

