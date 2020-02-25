# import os

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

"""
    3. Реализуйте классы Figure, Rectangle, Ellipse. Нужен метод получения
    координат x, y, размеров фигур w и h, также нужно, чтобы можно было
    получить периметр и площадь фигуры. Интерфейс Figure определить из
    файла figure_painter.py, т.е. изучаете код, а затем пишете интерфейс класса
    Figure так, чтобы он работал. Для запускай файла figure_painter.py
    необходимо установить библиотеку pip install pyside2. (Тема 2. Слайды 44-47)

    4. Переработайте иерархию классов Figure так, чтобы можно было рисовать
    произвольные замкнутые фигуры CloseFigure. Если Rectangle или Ellipse, то
    использовать другие методы, а не данные из CloseFigure.
"""


# Импортируйте свой файл с фигурами

class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур pu200')
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):
        painter = QPainter(self)
        reset_brush = painter.brush()
        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x(), figure.y(), figure.width(), figure.height())
                continue

            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x(), figure.y(), figure.width(), figure.height())
                continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))
                points = []
                for point in figure:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue


class Figure:
    def __init__(self, x, y):
        self._x = x
        self._y = y


    def x(self):
        return self._x

    def y(self):
        return self._y




class FigureHW(Figure):
    def __init__(self, x, y, h, w):
        super().__init__(x, y)
        self._h = h
        self._w = w

    def width(self):
        return self._w

    def height(self):
        return self._h

    def get_square(self):
        raise NotImplementedError

    def get_perimetr(self):
        raise NotImplementedError


class Rectangle(FigureHW):
    def __init__(self, x, y, h, w):
        super().__init__(x, y, h, w)

    def get_square(self):
        return self._h * self._w

    def get_perimetr(self):
        return (self._h + self._w) * 2



class Ellipse(FigureHW):
    def __init__(self, x, y, h, w):
        super().__init__(x, y, h, w)

    def get_square(self):
        return 3.1415 * self._h * self._w

    def get_perimetr(self):
        return 4 * (3.1415 * (self._h + self._w) + (self._h - self._w) ** 2 / (self._h + self._w))



class CloseFigure(Figure):
    def __init__(self, *points):
        assert len(points) >= 3
        super().__init__(points[0]['x'], points[0]['y'])
        self._points = points
        # print(f'x init:{self._x} y init:{self._y}')

    def __iter__(self):
        return iter(self._points)

    def get_perimetr(self):
        return None
        # raise NotImplementedError

    def get_square(self):
        return None
        # raise NotImplementedError


if __name__ == '__main__':
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур

    fig1 = Rectangle(10, 10, 50, 30)
    fig2 = Rectangle(50, 110, 20, 80)
    fig3 = Ellipse(110, 200, 80, 190)

    fig4 = CloseFigure({'x': 110, 'y': 100}, {'x': 150, 'y': 50}, {'x': 350, 'y': 100})

    # fig4 = None

    figures = [fig1, fig2, fig3, fig4]

    for i in figures:
        print(f'{i} \t{i.get_perimetr()} \t{i.get_square()}')

    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())
