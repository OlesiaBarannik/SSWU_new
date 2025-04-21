from abc import ABC, abstractmethod


class BuilderInterface(ABC):
    """Інтерфейс для будівельника"""

    @abstractmethod
    def build_construction(self) -> None:
        pass


class WaiterInterface(ABC):
    """Інтерфейс для офіціанта"""

    @abstractmethod
    def serve_the_table(self) -> None:
        pass


class TeacherInterface(ABC):
    """Інтерфейс для вчителя"""

    @abstractmethod
    def check_hometask(self) -> None:
        pass


class Builder(BuilderInterface):
    """Клас будівельника"""

    def build_construction(self) -> None:
        print("Building a construction!")


class Waiter(WaiterInterface):
    """Клас офіціанта"""

    def serve_the_table(self) -> None:
        print("Serving the table")


class Teacher(TeacherInterface):
    """Клас вчителя"""

    def check_hometask(self) -> None:
        print("Checking students' homework")


# Приклад використання:
builder = Builder()
builder.build_construction()

waiter = Waiter()
waiter.serve_the_table()

teacher = Teacher()
teacher.check_hometask()