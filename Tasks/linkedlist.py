from weakref import ref
import json

class IStuctureDriver:


    def read(self):
        ...

    def write(self):
        ...



class JSONFileDriver(IStuctureDriver):
    def __init__(self, filename):
        self._filename = filename


    def write(self, dct):
        print(dct)
        with open(self._filename, "w") as fp:
            json.dump(fp, dct)


    # def read(self):
    #     with open(self._filename, "r") as file:
    #         dct = json.load()
    #     print(f'load_json: {dct}; file:{self._filename}')
    #     return dct



class Node:
    def __init__(self, prev_node=None, next_node=None, data=None):

        if prev_node is not None and not isinstance(prev_node, type(self)):
            raise TypeError('prev_node must be Node or None')

        if next_node is not None and not isinstance(next_node, type(self)):
            raise TypeError('next_node must be Node or None')

        self.prev_node_ = ref(prev_node) if prev_node is not None else None
        self.next_node_ = next_node
        self.data = data

    @property
    def prev_node(self):
        return self.prev_node_() if self.prev_node_ is not None else None

    @prev_node.setter
    def prev_node(self, value):
        if value is not None and not isinstance(value, type(self)):
            raise TypeError('Value must be Node or None')
        self.prev_node_ = ref(value) if value is not None else None

    @property
    def next_node(self):
        return self.next_node_

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, type(self)):
            raise TypeError('Value must be Node or None')
        self.next_node_ = value


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.__structure_driver = None

        
    def insert_next_node(self, current_node, data):        
        new_node = Node(current_node, current_node.next_node, data)
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        self.size += 1
        
    def insert_node(self, index, data):
        if not isinstance(index, int):
            raise TypeError('index must be int')        
        
        if index >= 0:    
            if not 0 <= index < self.size:
                raise ValueError('Invalid index')
            current_node = self.head.next_node
            for _ in range(self.size):
                current_node = current_node.next_node
                
            self.insert_next_node(current_node, data)

    def append(self, data):
        new_node = Node(data=data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
            self.size += 1

    # def get(self, index=0):
    #     return self.

    def set_structure_driver(self, stucture_driver):
        self.__structure_driver = stucture_driver


    def save(self):
        i = 0
        _current_node: Node = ll.head
        save_dict = {}
        # print('save list:')
        while i < self.size:
            save_dict[id(_current_node)] = {
                                            'data': _current_node.data ,
                                            'prev': id(_current_node.prev_node_) if _current_node.prev_node_ else None,
                                            'next': id(_current_node.next_node_) if _current_node.next_node_ else None
                                            }
            # print(f'dict: {save_dict}')
            _current_node = _current_node.next_node
            i += 1
        # return save_dict
        if isinstance(self.__structure_driver, IStuctureDriver):
            self.__structure_driver.write(save_dict)
        else:
            raise TypeError('Err "structure_driver" must be IStuctureDriver')




    def load(self):
        load_dict = {}
        if isinstance(self.__structure_driver, IStuctureDriver):
            load_dict = self.__structure_driver.read()
            print(f' load_1: {load_dict} driver:  {self.__structure_driver} jsonFile:{self.__structure_driver._filename}')
        else:
            raise TypeError('Err "structure_driver" must be IStuctureDriver')
        print(f'res load_2: {load_dict}')
        # self.clear -- метод очистки должен быть реализован
        self.tail = None
        self.head = None
        self.size = 0
        # current_node =




            
        
        # if index < 0:
        #     ...
        #
        
            
ll = LinkedList()

# ll.insert_node(0, 'Привет')
# ll.insert_node(1, 'Python')

ll.append("Привет")
# print(f'id:{id(ll.head)},  data:{ll.head.data};  \t\tnext:{ll.head.next_node},  \tprev:{ll.head.prev_node}')
ll.append("Python")
ll.append("Foo")
ll.append("Bar")

#
# i = 0
# current_node: Node = ll.head
# while i < ll.size:
#     print(f'id:{id(current_node)},  data:{current_node.data},  \tprev:{current_node.prev_node};  \t\tnext:{current_node.next_node}')
#     current_node = current_node.next_node
#     i += 1
#
ll.set_structure_driver(JSONFileDriver('PU200json.txt'))
print(ll.save())

# ll.load()


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



        
        
        
        
        
        
        
        
        
   