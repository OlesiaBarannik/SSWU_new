from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Абстрактний базовий клас для фігур, що підтримують обчислення площі.

    OOP: Абстракція — визначає інтерфейс без реалізації.
    SOLID: ISP (Interface Segregation Principle).
    """

    @abstractmethod
    def area(self, result_type: str = "float") -> float | int | str:
        pass

    def _convert_area(self, area: float, result_type: str) -> float | int | str:
        return int(area) if result_type == "int" else str(area) if result_type == "str" else area


class Triangle(Shape):
    """
    Обчислює площу трикутника.

    OOP: Наслідування від Shape, Інкапсуляція через метод is_valid.
    SOLID: LSP (Liskov Substitution Principle) — можна підставити Triangle замість Shape.
    """

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def area(self, result_type: str = "float") -> float | int | str:
        if not self.is_valid():
            return "Неприпустимі сторони трикутника"
        p = (self.a + self.b + self.c) / 2
        return self._convert_area(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), result_type)


class Rectangle(Shape):
    """
    Клас для прямокутника.

    OOP: Наслідування, Інкапсуляція.
    SOLID: LSP.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self, result_type: str = "float") -> float | int | str:
        return self._convert_area(self.width * self.height, result_type)


class AreaWriter:
    """
    Клас для збереження площ фігур у текстові файли.

    OOP: Інкапсуляція — логіка збереження прихована в методі.
    SOLID: SRP (Single Responsibility Principle).
    """

    def __init__(self, shape_name: str, area: float | int | str):
        self.shape_name = shape_name
        self.area = area

    def to_txt(self) -> None:
        try:
            with open(f"{self.shape_name}_area.txt", "w", encoding="utf-8") as file:
                file.write(f"Площа {self.shape_name}: {self.area}")
        except Exception as e:
            print(f"Сталася помилка: {e}")
        else:
            print(f"Площа {self.shape_name} успішно збережена у файл")
        finally:
            print("Завершено")