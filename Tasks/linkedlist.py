from weakref import ref
import json


"""
Лабораторная работа № 3 
февраль 2020
Пантелеев А.В.
"""
class IStuctureDriver:


    def read(self):
        ...

    def write(self, dct):
        ...



class JSONFileDriver(IStuctureDriver):
    def __init__(self, filename):
        self._filename = filename


    def write(self, dct):
        with open(self._filename, "w") as fp:
            json.dump(dct, fp)


    def read(self):
        with open(self._filename, "r") as fp:
            dct = json.load(fp)
        return dct


class Subject():
    def add_observer(self):
        ...


class Data(Subject):
    ...


class Observer:
    def update(self):
        ...


class Node:
    def __init__(self, prev_node=None, next_node=None, data=None):
        self.prev_node = prev_node
        self.next_node = next_node
        self.data = data
        # print(f'init Node:{self.prev_node}')

    def __eq__(self, other):
        if not isinstance(other, (Node, type(self.data))):
            return NotImplemented

        if isinstance(other, type(self.data)):
            return self.data == other

        return self.data == other.data

    @property
    def prev_node(self):
        return self.prev_node_() if self.prev_node_ is not None else None

    @prev_node.setter
    def prev_node(self, value):
        if value is not None and not isinstance(value, type(self)):
            raise TypeError('next_node must be Node or None')
        self.prev_node_ = ref(value) if value is not None else None

    @property
    def next_node(self):
        return self.next_node_

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, type(self)):
            raise TypeError('Value must be Node or None')
        self.next_node_ = value


class LinkedList(Observer):

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.__structure_driver = None

    # def insert_next_node(self, current_node, data):
    #     new_node = Node(current_node, current_node.next_node, data)
    #     current_node.next_node.prev_node = ref(new_node)
    #     current_node.next_node = new_node
    #     self.size += 1
        
    def insert_node(self, index, data):
        if not isinstance(index, int):
            raise TypeError('index must be int')
        if not 0 <= index <= self.size - 1:
            raise ValueError('Invalid index')
        i = 0
        current_node = self.head
        while i < index:
            current_node = current_node.next_node
            i += 1

        if index == 0:
            new_node = Node(None, self.head, data)
            self.head.prev_node = new_node
            self.head = new_node
        elif index == self.size - 1:
            self.tail.next_node = Node(self.tail, None, data)
            self.tail = self.tail.next_node
        else:
            current_node.prev_node.next_node = Node(current_node.prev_node, current_node.next_node, data)
            current_node.next_node.prev_node = current_node.prev_node.next_node
        self.size += 1



    def append(self, data):
        """
        добавляет новую ноду с данными
        """
        new_node = Node(data=data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

        self.size += 1


    def find(self, node):
        """
        выдает индекс ноды переданную параметром
        """
        _current_node: Node = self.head
        i = 0
        while i < self.size:
            if _current_node == node:
                return i
            _current_node = _current_node.next_node
            i += 1


    def remove(self, node):
        """
        удаляет ноду переданную параметром
        """
        _current_node: Node = self.head
        i = 0

        while i < self.size:
            if _current_node == node:
                # НЕ последний элемент
                if _current_node.next_node:
                    _current_node.next_node.prev_node = _current_node.prev_node
                else:
                    self.tail = _current_node.prev_node
                # НЕ первый элемент
                if _current_node.prev_node:
                    _current_node.prev_node.next_node = _current_node.next_node
                else:
                    self.head = _current_node.next_node
                self.size -= 1

                # нужно ли очищать удаляемую ноду ??
                _current_node.data = None
                _current_node.prev_node = None
                _current_node.next_node = None
                print(f'remove(self, {node})  COMLETE')
                return
            _current_node = _current_node.next_node
            i += 1
        print(f'remove data:{node.data}(self, {node})  Not COMLETE ')



    def delete(self, index):
        """
        удаляет ноду с заданным в параметрах индексом
        """
        _current_node: Node = self.head
        i = 0
        if index > self.size:
            raise IndexError('index more then len')
        while i < index - 1:
            _current_node = _current_node.next_node
            i += 1
        # НЕ последний элемент
        if _current_node.next_node:
            _current_node.next_node.prev_node = _current_node.prev_node
        else:
            self.tail = _current_node.prev_node
        # НЕ первый элемент
        if _current_node.prev_node:
            _current_node.prev_node.next_node = _current_node.next_node
        else:
            self.head = _current_node.next_node
        self.size -= 1

        # нужно ли очищать удаляемую ноду ??
        _current_node.data = None
        _current_node.prev_node = None
        _current_node.next_node = None
        print(f'delete(self, {index})  COMLETE')




    def set_structure_driver(self, stucture_driver):
        self.__structure_driver = stucture_driver


    def save(self):
        i = 0
        _current_node: Node = self.head
        save_dict = {}
        # print('save list:')
        while i < self.size:
            # save_dict[id(_current_node)] = {
            #                                 'data': _current_node.data,
            #                                 'prev': id(_current_node.prev_node_) if _current_node.prev_node_ else None,
            #                                 'next': id(_current_node.next_node_) if _current_node.next_node_ else None
            #                                 }
            save_dict[i] = {
                                            'data': _current_node.data,
                                            'prev': i - 1 if _current_node.prev_node_ else None,
                                            'next': i + 1 if _current_node.next_node_ else None
                                            }
            # print(f'dict: {save_dict}')
            _current_node = _current_node.next_node
            i += 1
        # return save_dict
        if isinstance(self.__structure_driver, IStuctureDriver):
            self.__structure_driver.write(save_dict)
        else:
            raise TypeError('Err "structure_driver" must be IStuctureDriver')


    def clean(self):
        self.tail = None
        self.head = None
        self.size = 0

    def load(self):
        if isinstance(self.__structure_driver, IStuctureDriver):
            load_dict = self.__structure_driver.read()
        else:
            raise TypeError('Err "structure_driver" must be IStuctureDriver')

        # метод очистки должен быть реализован
        self.clean()

        i = 0

        for node in load_dict.items():
            print(f"ns:  {i} index:{node[0]} \tnode : {node} ")
        for node in sorted(load_dict.items()):
            print(f'i:  {i} \tnode : {node}')
            self.append(node[1]['data'])
            # if i == 0:
            #     self.append(node[1]['data'])
            # else:
            #     self.append(node[1]['data'], node[1]['data'] )

            i += 1
        print(f'load(self) Complete, load: {i+1} Node ')




#   ##########################################################
#   ##########################################################
#   ##########################################################
#   ##########################################################
            
ll = LinkedList()

# ll.insert_node(0, 'Привет')
# ll.insert_node(1, 'Python')

ll.append("Привет")
ll.append("Python")
ll.append("Foo")
ll.append("Bar")
ll.append("PredLast")
ll.append("Last")
# del_test_node = Node('Last22')
#
# i = 0
# current_node: Node = ll.head
# while i < ll.size:
#     print(f'id:{id(current_node)},  data:{current_node.data},  \tprev:{current_node.prev_node};  \t\tnext:{current_node.next_node}')
#     current_node = current_node.next_node
#     i += 1
#
ll.set_structure_driver(JSONFileDriver('PU200json.txt'))


print(f'\nLL size:{ll.size} head:{ll.head} tail:{ll.tail}')
ii = 0
test_current_node: Node = ll.head
while ii < ll.size:
    if ii == ll.size - 1:
        del_node = test_current_node
    print(f'{ii} id:{id(test_current_node)},  data:{test_current_node.data},  \tprev:{test_current_node.prev_node};  \t\tnext:{test_current_node.next_node}')
    # print(f'type pref:{type(current_node.prev_node)}')
    test_current_node = test_current_node.next_node

        # print(f'DelNode: {del_node}')
    ii += 1

# ll.save()             # work
# ll.delete(2)          # work
# ll.clean()            # work
ll.remove(del_node)     # work


print('\nLoad ...')
ll.load()

# ll.delete(0)  # work
# ll.delete(ll.size)  # work
# ll.delete(ll.size)  # work

ll.insert_node(0, 'test00')     #work
# ll.insert_node(1, 'test00')     #work
ll.insert_node(ll.size - 1, 'test333')      #work -- its last

print(f'\nAfter delete/load; size:{ll.size} head:{ll.head} tail:{ll.tail}')
ii = 0
test_current_node: Node = ll.head
while ii < ll.size:
    print(f'{ii} id:{id(test_current_node)},  data:{test_current_node.data},  \tprev:{test_current_node.prev_node};  \t\tnext:{test_current_node.next_node}')
    # print(f'type pref:{type(current_node.prev_node)} type node:{type(current_node)}')
    test_current_node = test_current_node.next_node
    ii += 1



"""
Вопросы:
1. ll.remove(del_node) - можно через данные реализовать или таки через Ноду ???
2. Можно верить последовательности из сохранения или нужно проверял next/prev from save
3. Нужно очищать содержимое при удалении ??
"""


"""
В качестве входного параметра используется словарь. Для упрощения работы с
алгоритмами сохранения и чтения данных необходимо разработать некоторый объект,
который будет себя вести как словарь. Данный подход применим в следующей
лабораторной работе (шаблон проектирования «Заместитель»), потому что для
использования данного шаблона для LinkedList необходимо уметь перегружать встроенные
операторы. Сейчас поступим следующим образом. Добавьте методы LinkedList.save и
LinkedList.load. В этих методах сделайте преобразование из LinkedList в словарь. В
результате будет следующая диаграмма классов. Код IStructureDriver и всех наследников
не меняется.
"""


        
        
        
        
        
        
        
        
        
   