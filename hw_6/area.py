from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Абстрактний базовий клас для фігур, що підтримують обчислення площі.
    """

    @abstractmethod
    def area(self, result_type: str = "float") -> float | int | str:
        """
        Метод для обчислення площі фігури.
        Має бути перевизначений у підкласах.
        """
        pass

    def _convert_area(self, area: float, result_type: str) -> float | int | str:
        """
        Допоміжний метод для перетворення площі в зазначений тип.
        """
        if result_type == "int":
            return int(area)
        elif result_type == "str":
            return str(area)
        return area

class Triangle(Shape):
    """
    Обчислює площу трикутника.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        Ініціалізує трикутник з трьома сторонами.
        """
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        """
        Перевіряє, чи є трикутник валідним (сума двох сторін повинна бути більшою за третю).
        """
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def area(self, result_type: str = "float") -> float | int | str:
        """
        Площу трикутника за формулою Герона.
        """
        if not self.is_valid():
            return "Неприпустимі сторони трикутника"
        else:
            p = (self.a + self.b + self.c) / 2
            area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return self._convert_area(area, result_type)


class Rectangle(Shape):
    """
    Клас для прямокутника.
    """

    def __init__(self, width: float, height: float):
        """
        Ініціалізує прямокутник за шириною та висотою.
        """
        self.width = width
        self.height = height

    def area(self, result_type: str = "float") -> float | int | str:
        """
        Обчислює площу прямокутника.
        """
        area = self.width * self.height
        return self._convert_area(area, result_type)


class AreaWriter:
    """
    Клас для збереження площ фігур у текстові файли.
    """

    def __init__(self, shape_name: str, area: float | int | str):
        self.shape_name = shape_name
        self.area = area

    def to_txt(self) -> None:
        """
        Записує площу фігури у файл з назвою {назва_фігури}_area.txt.
        """
        try:
            with open(f"{self.shape_name}_area.txt", "w", encoding="utf-8") as file:
                file.write(f"Площа {self.shape_name}: {self.area}")
        except Exception as e:
            print(f"Сталася помилка під час створення .txt файлу: {e}")
        else:
            print(f"{self.shape_name} площа успішно збережена у файл {self.shape_name}_area.txt")
        finally:
            print("Завершено.")