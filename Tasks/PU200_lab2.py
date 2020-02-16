"""
    15.02.2020

    1 В Python нет возможности объявления константных переменных. Реализуйте
    с помощью @property константный атрибут. Пусть класс возвращает число
    пи. Попытайтесь применить @property к @staticmethod и @classmethod. Если
    не получается, то примените к обычному методу. (Тема 1. Слайды 1-43)



    3. Реализуйте классы Figure, Rectangle, Ellipse. Нужен метод получения
    координат x, y, размеров фигур w и h, также нужно, чтобы можно было
    получить периметр и площадь фигуры. Интерфейс Figure определить из
    файла figure_painter.py, т.е. изучаете код, а затем пишете интерфейс класса
    Figure так, чтобы он работал. Для запускай файла figure_painter.py
    необходимо установить библиотеку pip install pyside2. (Тема 2. Слайды 44-47)

    4. Переработайте иерархию классов Figure так, чтобы можно было рисовать
    произвольные замкнутые фигуры CloseFigure. Если Rectangle или Ellipse, то
    использовать другие методы, а не данные из CloseFigure.

    5. В Python 3 все классы являются классами нового стиля. Классы нового стиля
    – это классы, которые являются наследниками от класса object. Убедитесь,
    что класс А является наследником от object. (Тема 2. Слайды 48-52)
"""


class Pi:
    # последовательность декораторов ВАЖНА
    # @property используем сами по себе, без  @staticmethod и  @classmethod


    @property
    # в свойствах не может быть аргументов кроме self
    # и без setter его никак нельзя менять !!!!!!!!!
    # и можно вызывать без СКОБОК ибо не метод, атрибут
    # и работает это для экземпляра класса, не для класса!
    def get_pi(self):
        return 3.141592

    # можно применять к классу, не обязательно к экземпляру класса
    @staticmethod
    @property
    def get_pi2():
        return 3.141592

    @property
    @classmethod
    def get_pi3(cls):
        return 3.141592
#
#
# a = Pi()
#
# print(a.get_pi)
# # a.get_pi = 42
# print(a.get_pi)
#
# # print(Pi().get_pi2)
# # print(Pi().get_pi3)
#

""" 
    2. Создайте классы A и B(A). 
        a. В классе А создайте атрибуты класса, атрибуты 
    объекта, @staticmethod, @classmethod и методов со всеми видами областями
    видимости. 
        b. Продемонстрируете их видимость внутри класса, вне класса и в
    классе потомке. 
        c. Получите доступ вне класса к псевдозащищённым
    псевдоприватным атрибутам и методам. (Тема 2. Слайды 1-43)

"""


class A:
    # это есть Атрибуты от КЛАССА !!!!!!!!!, не объекта (не экземпляра)
    # НО это хорошо действует для изменяемых типов - например список и добавляем в него
    # а если присваиваем "в лоб" можем словить разныве варианты - нужно учитывать
    # если хотим менять атрибут класса, лучше обращаться через Класс, а не объект !!
    class_attribute = [123]
    __class_attribute_2 = ['cls_attrib']

    def __init__(self, num, num2):
        self.attribute_1 = num + 1          # NORMAL
        self._attribute_1 = num + 2         # protected
        self.__attribute_1 = num + 3        # PRIVATE !!! - он переименовывается c учетом класса
        self.attribute_2 = num2 + 1  # NORMAL


    @staticmethod
    def get_attrib_1():
        # return 'qwer'
        return A.class_attribute

    @classmethod
    def get_attrib_2(cls):
        return cls.__class_attribute_2


class B(A):
    ...
    def __init__(self, num, num2):
        # super().__init__(num, num2)
        super().__init__()
        self.attribute_b = num + 10          # NORMAL
        self._attribute_b = num + 2         # protected
        self.__attribute_b = num + 3        # PRIVATE !!! - он переименовывается




varA = B(10, 3)
varB = B(22, 3)

# print(varA.class_attribute)
# varA.class_attribute = 'new value'
# print(varA.class_attribute)
#
# # интерпретатор приватные переменные переименовывает через имя класса, только так его можно вытащить
# print(varA._A__class_attribute_2)
# varA._A__class_attribute_2 = 'new value2'
# print(varA._A__class_attribute_2)

print(f'A id:{id(varA.class_attribute)}')
print(f'B id:{id(varB.class_attribute)}')

print(f'A:{varA.class_attribute}')
print(f'B:{varB.class_attribute}')

varA.class_attribute.append(73)
print(f'A:{varA.class_attribute}')
print(f'B:{varB.class_attribute}')

varA.class_attribute = 13
print(f'A:{varA.class_attribute}')
print(f'B:{varB.class_attribute}')
print(f'A dict:{varA.__dict__}')
print(f'B dict:{varB.__dict__}')
A.class_attribute = 55
print(f'A:{varA.class_attribute}')
print(f'B:{varB.class_attribute}')

varC = A(11, 0)
print(f'C:{varB.class_attribute}')

print(f'A id:{id(varA.class_attribute)}')
print(f'B id:{id(varB.class_attribute)}')
print(f'C id:{id(varC.class_attribute)}')

print(f'\tA get1:{varA.get_attrib_1()}')
# print(f'A get2:{A.get_attrib_2}')

var3 = B(17, 0)

# print(f'A:{varA.class_attribute}')
print(f'B dict:{var3.__dict__}, {var3}')
print(f'B attrib from A; 1:{var3.attribute_1} 2:{var3.attribute_2} ')
print(f'B dict:{var3.get_attrib_2()}')