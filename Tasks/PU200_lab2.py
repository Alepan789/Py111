"""
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
    2. Создайте классы A и B(A). a. В классе А создайте атрибуты класса, атрибуты
    объекта, @staticmethod, @classmethod и методов со всеми видами областями
    видимости. b. Продемонстрируете их видимость внутри класса, вне класса и в
    классе потомке. c. Получите доступ вне класса к псевдозащищённым
    псевдоприватным атрибутам и методам. (Тема 2. Слайды 1-43)

"""


class A:
    class_attribute = 'cls_attrib'
    __class_attribute_2 = 'cls_attrib'

    def __init__(self, num):
        self.attribute_1 = num + 1          # NORMAL
        self._attribute_2 = num + 2         # protected
        self.__attribute_3 = num + 3        # PRIVATE !!! - он переименовывается


    def get_attrib_1(self):
        return self.attribute_1



class B(A):
    ...

varA = A()
print(varA.class_attribute)
varA.class_attribute = 'new value'
print(varA.class_attribute)

# интерпретатор приватные переменные переименовывает через имя класса, только так его можно вытащить
print(varA._A__class_attribute_2)
varA._A__class_attribute_2 = 'new value2'
print(varA._A__class_attribute_2)