
# 11. Циклическая зависимость (стр. 39-44)
#

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
        # print(f'id:{id(self)} self:{self}')

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        return f'Node: prev:{self.__prev} next:{self.__next}'
        # return f'Node: {self})'

    def __repr__(self):
        return f'Node({self.__prev}, {self.__next})'


class LinkedList:
    def __init__(self):
        self.__lst = []


    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        # node.set_prev()
        # node.set_next()

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        node.set_next(0)
        node.set_prev(-1)
        self.__lst.append(node)
        print(f'append:\tlist:{self}\t{node}')

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...

# lst = LinkedList()
# lst.append(Node())
# lst.append(Node())
#
# lst2 = LinkedList()
# lst2.append(Node())
# lst2.append(Node())


a = Node()
b = Node()
print(a.__dict__, id(a))
print(b.__dict__, id(b))
print(a)

class Tst:
    def __init__(self, v1=None, v2=None):
        self.v1 = v1
        self.v2 = v2
        # print(self.__dict__)

    def __str__(self):
        # return f'Node: {self}; prev:{self.__prev} next:{self.__next})'
        return f'Tst: {self.v1})'


s1 = Tst()
print(s1)


