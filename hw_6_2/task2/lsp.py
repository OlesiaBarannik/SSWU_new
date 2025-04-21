from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Базовий клас для всіх транспортних засобів"""

    @abstractmethod
    def move(self) -> None:
        pass


class EngineVehicle(Vehicle):
    """Базовий клас для транспортних засобів з двигуном"""

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(EngineVehicle):
    def move(self) -> None:
        print("Car is moving")

    def start_engine(self) -> None:
        print("Engine started")


class Bicycle(Vehicle):
    def move(self) -> None:
        print("Bicycle is moving using pedals")


# Приклад використання:
car = Car()
bicycle = Bicycle()
car.move()
car.start_engine()
bicycle.move()