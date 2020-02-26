# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Пантелеев А.В. 2019-2020год

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

import weakref as ref

class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError('Argument must be int/float')
        if capacity_volume < 0:
            raise ValueError('Argument must be positive or zero')

        if not isinstance(occupied_volume, int):
            raise TypeError('Argument must be int')
        if occupied_volume < 0:
            raise ValueError('Argument must be positive or zero')

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __str__(self):
        return f'Glass({self.capacity_volume}, {self.occupied_volume})'

    def __repr__(self):
        # подробное описание
        return f'Capacity_volume:{self.capacity_volume} \t Occupied_volume:{self.occupied_volume}'


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

glass1 = Glass(100, 200)
print(glass1)
print(glass1.__repr__())

# glass2 = Glass(-10, 'qwe')
# glass2 = Glass(100, 'qwe')
# glass2 = Glass(-10, False)
glass2 = Glass(35.5, 5)

# print(f"glass1 p1:{glass1.__str__}")
print(f"glass1 :{glass1} \t\t glass2 :{glass2}")
# print(f"glass2 :{glass2}")

glass2.occupied_volume = 50
print(f"glass1 :{glass1} \t\t glass2 :{glass2}")


# print(f"glass2 :{glass2}")

# print(f"glass1 p1:{glass1.__str__}")
# print(f"glass1 p1:{glass1.__dict__}")


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        if not isinstance(occupied_volume, int):
            raise TypeError('Argument must be int')

        if occupied_volume < 0:
            raise ValueError('Argument must be positive or zero')

        self.occupied_volume = occupied_volume

    def __str__(self):
        return f'{__class__}::: Occupied_volume:; {self.occupied_volume}'


glass10 = GlassDefaultArg(50)
print('\nGlass 10', glass10)

glass20 = GlassDefaultArg()
print('Glass 20', glass20)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

# ответ - нельзя ибо если повторно создавать несколько объектов со значением по умолчанию
# будем получать во всех последующих наследование начально изменных данных


class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        # надо делать такую магию
        # occupied_volume = None
        # occupied_volume = occupied_volume or []   # здесь по результатам получаем если False то []
        # occupied_volume.append(2)

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError('Argument must be int/float')

        if capacity_volume < 0:
            raise ValueError('Argument must be positive or zero')

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)

    def __str__(self):
        return f'{__class__}: Capacity_volume:{self.capacity_volume};;;  occupied_volume:{self.occupied_volume}'


glass4_1 = GlassDefaultListArg(0)
print(f'\n{glass4_1}')
glass4_1.occupied_volume.append(3)
print(f'{glass4_1}')
glass4_1.occupied_volume.append(30)
print(f'{glass4_1}')

glass4_2 = GlassDefaultListArg(10)
print(f'\n glass4_2')
print(f'{glass4_2}')
glass4_2.occupied_volume.append(50)
print(f'{glass4_2}')
glass4_2.occupied_volume.append(100)
print(f'{glass4_2}')

glass4_3 = GlassDefaultListArg(20)
print(f'\n glass4_3')
print(f'{glass4_3}')
glass4_3.occupied_volume.append(30)
print(f'{glass4_3}')
glass4_3.occupied_volume.append(40)
print(f'{glass4_3}')


#
#
# glass4_20 = GlassDefaultListArg(100)
# print(f'\n{glass4_20}')
# glass4_20.occupied_volume.append(12)
# print(f'{glass4_20}')
# glass4_20.occupied_volume.append(112)
# print(f'{glass4_20}')


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.


class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError('Argument must be int/float')
        if capacity_volume < 0:
            raise ValueError('Argument must be positive or zero')

        if not isinstance(occupied_volume, int):
            raise TypeError('Argument must be int')
        if occupied_volume < 0:
            raise ValueError('Argument must be positive or zero')

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __str__(self):
        return f'Glass({self.capacity_volume}, {self.occupied_volume})'

    def __repr__(self):
        return f'Capacity_volume:{self.capacity_volume} \t Occupied_volume:{self.occupied_volume}'
    
    def add_water(self, qty):
        if not isinstance(qty, int):
            raise TypeError('Add argument must be int')

        if self.occupied_volume + qty > self.capacity_volume or qty < 0:
            raise ValueError('Summary volume more then capacity_volume or qty<0')

        self.occupied_volume += qty
        print(f'after add_water  qty:{qty}:: \tCapacity_volume:{self.capacity_volume} \t Occupied_volume:{self.occupied_volume}')

    def remove_water(self, qty):
        if not isinstance(qty, int):
            raise TypeError('Add argument must be int')

        if self.occupied_volume - qty < 0 or qty < 0:
            raise ValueError('Summary volume < 0 or qty<0')

        self.occupied_volume -= qty
        print(f'after remove_water qty:{qty}: \tCapacity_volume:{self.capacity_volume} \t Occupied_volume:{self.occupied_volume}')


glass5_1 = GlassAddRemove(500, 250)
print(f'\n glass5_1')
print(f'{glass5_1}')
glass5_1.add_water(50)
glass5_1.add_water(200)
print(f'{glass5_1}')
glass5_1.remove_water(150)
glass5_1.remove_water(200)
print(f'{glass5_1}')


# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.


glass5_2 = GlassAddRemove(350, 150)
glass5_3 = GlassAddRemove(250, 250)
print(glass5_1.__dir__())
print(dir(glass5_2))
print(dir(glass5_3))
print(type(glass5_1.capacity_volume))
print(type(glass5_1))
print(isinstance(glass5_1.capacity_volume, int))
print(isinstance(glass5_1.occupied_volume, int))
print(isinstance(glass5_1, GlassAddRemove))

# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.


class Example7:
    def __init__(self, var1, var2):
        print(f'start:\t{self.__dict__}')

        if not isinstance(var1, (int, float)):
            raise TypeError('Argument must be int/float')

        if not isinstance(var2, (int, float)):
            raise TypeError('Argument must be int/float')


        self.var1 = var1
        print(f'middle:\t{self.__dict__}')
        self.var2 = var2

        print(f'end:\t{self.__dict__} ')

    def __str__(self):
        return f'Glass({self.var1}, {self.var2})'


#    Опишите результат.
# получаем "объявленную" и заполненную переменную только после завершения инициализации


var_example71 = Example7(10, 20)

print(f'ЭКЗ:\t{var_example71.__dict__}')
# print(str(var_example71))

# var_example72 = Example7(20, 20)




# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.
class Glass1:
    def __init__(self):
        print(f'self:\t{id(self)}')
        self.capacity_volume = 50

print(f'\nСоздайте три объекта Glass id для каждого объекта с соответсвующим id переменной self')
glass1_1 = Glass1()
print(f'экз\t\t{id(glass1_1)}')
glass1_2 = Glass1()
print(f'экз\t\t{id(glass1_2)}')
glass1_3 = Glass1()
print(f'экз\t\t{id(glass1_3)}')

# итого
# id переменной self совпадает, то есть экземпляр и есть фактически self


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python; -
#     - соглашения о стиле кодирования
#    Запустите код.
# - корректно
# - НеКорректно


class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)


d.print_me(d())


# 10. Исправьте
# class A:
#     def __init__(self, a):
#         if 10 < a < 50:
#             return
#         self.a = a;

# Объясните так реализовывать __init__ нельзя?
# нельзя, после raise происходит выход и присвоения не происходит

class A:
    def __init__(self, a):
        if 10 < a < 50:
            raise ValueError('Argument must be another')
        self.a = a





# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, prev=None, next_=None, data=None):
        self.__prev = prev
        self.__next = next_
        self.data = data

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        return f'Node; prev:{self.__prev} next:{self.__next} data:{self.data})'

    def __repr__(self):
        return f'Node({self.__prev}, {self.__next}, {self.data})'


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


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
        node.set_prev(id(self.tail))
        self.tail=id(node)
        node.set_next(None)
        self.size += 1
        print(f'append:\tlist:{self}\t{node}')

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...
        self.tail = None
        self.head = None
        self.size = 0

    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...

lst = LinkedList()
lst.append(Node())
lst.append(Node())

lst2 = LinkedList()
lst2.append(Node())
lst2.append(Node())