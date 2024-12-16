# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Measurement:
    """
    Класс описывает измерения модели колонки
    """
    def __init__(self, length_edge: Union[int, float], width_edge: Union[int, float], height_edge: Union[int, float]):
        """
        Инициализация экземпляра класса описывает измерения колонки в форме прямоугольного параллелепипеда
        :param length_edge: длина грани
        :param width_edge: ширина грани
        :param height_edge: высота грани
        проверяем, что длина грани типа int или float и положительное число
        проверяем, что ширина грани типа int или float и положительное число
        проверяем, что высота грани типа int или float и положительное число
        В ином случае вызываем ошибки
        """
        if not isinstance(length_edge, (int, float)):
            raise TypeError("Длина грани должна быть типа int или float")
        if length_edge <= 0:
            raise ValueError("Длина грани должна быть положительным числом")
        self.length_edge = length_edge
        if not isinstance(width_edge, (int, float)):
            raise TypeError("Ширина грани должна быть типа int или float")
        if width_edge <= 0:
            raise ValueError("Ширина грани должна быть положительным числом")
        self.width_edge = width_edge
        if not isinstance(height_edge, (int, float)):
            raise TypeError("Высота грани должна быть типа int или float")
        if height_edge <= 0:
            raise ValueError("Высота грани должна быть положительным числом")
        self.height_edge = height_edge

    def area(self) -> Union[int, float]:
        """
        Функция, которая считает площадь колонки
        :return: Значение площади колонки
        Пример:
        >>> measure = Measurement(3, 2, 5)
        >>> measure.area()
        6
        """
        return self.length_edge * self.width_edge

    def volume(self, area) -> Union[int, float]:
        """
        Функция, которая считает объем колонки
        :return: Значение объема колонки
        Пример:
        >>> measure = Measurement(3, 2, 5)
        >>> measure.volume(area=measure.area())
        30
        """
        return area*self.height_edge


class Color:
    def __init__(self, color_body: int, color_lighting: int):
        """
        Инициализация экземпляра класса описывает цвета корпуса и подсветки колонки
        :param color_body: значение цвета корпуса
        :param color_lighting: значение цвета подсветки
        проверяем, что значения цвета типа int и в диапазоне от 0 до 255
        В ином случае вызываем ошибки
        """
        if not isinstance(color_body, int):
            raise TypeError("Цвет должен быть типа int")
        if not 255 >= color_body >= 0:
            raise ValueError("Цвет должен быть в диапазоне от 0 до 255 для 8-битной шкалы цветового кода")
        self.color_body = color_body
        if not isinstance(color_lighting, int):
            raise TypeError("Цвет должен быть типа int")
        if not 255 >= color_lighting >= 0:
            raise ValueError("Цвет должен быть в диапазоне от 0 до 255 для 8-битной шкалы цветового кода")
        self.color_lighting = color_lighting

    def change_color(self, new_value) -> int:
        """
        Функция, которая изменяет цвет подсветки колонки
        :param new_value: значение нового цвета
        :return: Измененное значение цвета подсветки
        Пример:
        >>> color1 = Color(10, 10)
        >>> color1.change_color(255)
        255
        """
        if not isinstance(new_value, int):
            raise TypeError("Цвет должен быть типа int")
        if not 255 >= new_value >= 0:
            raise ValueError("Цвет должен быть в диапазоне от 0 до 255 для 8-битной шкалы цветового кода")
        self.color_lighting = new_value
        return self.color_lighting

    def hex_color(self) -> str:
        """
        Функция, которая изменяет значение цвета в hex формат
        :return: Значение цвета в hex формат в виде #00
        Пример:
        >>> color1 = Color(10,255)
        >>> color1.hex_color()
        '#ff'
        """
        hex_lighting = hex(self.color_lighting)
        return "#" + hex_lighting[2:]


class Music:
    def __init__(self, max_volume: int, music_volume: int):
        """
        Инициализация экземпляра класса описывает громкость колонки
        :param music_volume: текущяя громкость
        :param max_volume: максимальное значение громкости
        проверяем, что максимальное значение громкости типа int и не отрицательное число
        проверяем, что текущяя громкость типа int, не отрицательное число и не больше максимального
        В ином случае вызываем ошибки
        """
        if not isinstance(max_volume, int):
            raise TypeError("Громкость должна быть типа int")
        if max_volume < 0:
            raise ValueError("Громкость должна быть не отрицательным числом")
        self.max_volume = max_volume
        if not isinstance(music_volume, int):
            raise TypeError("Громкость должна быть типа int")
        if not max_volume >= music_volume >= 0:
            raise ValueError("Громкость должна быть не отрицательным числом, и не может превышать максимальное")
        self.music_volume = music_volume

    def middle_volume(self) -> int:
        """
        Функция, которая считает среднюю громкость музыки
        :return: Средняя громкость колонки
        Пример:
        >>> music = Music(100,25)
        >>> music.middle_volume()
        50
        """
        return round(self.max_volume/2)

    def mute(self) -> int:
        """
        Функция, которая выключает звук
        :return: Выключенная громкость к
        Пример:
        >>> music = Music(100,25)
        >>> music.mute()
        0
        """
        self.music_volume = 0
        return self.music_volume


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
