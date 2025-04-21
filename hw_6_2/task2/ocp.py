from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Абстрактний базовий клас для різних стратегій знижок."""

    @abstractmethod
    def get_discount(self, price: float) -> float:
        """Метод для розрахунку суми знижки."""
        pass


class SilverDiscount(DiscountStrategy):
    """Стратегія для silver-клієнтів."""

    def get_discount(self, price: float) -> float:
        return price * 0.2  # 20% сума знижки


class GoldDiscount(DiscountStrategy):
    """Стратегія для gold-клієнтів."""

    def get_discount(self, price: float) -> float:
        return price * 0.3  # 30% сума знижки


class VIPDiscount(DiscountStrategy):
    """Стратегія для vip-клієнтів."""

    def get_discount(self, price: float) -> float:
        return price * 0.4  # 40% сума знижки


class Discount:
    """Клас для застосування певної стратегії знижки."""

    def __init__(self, strategy: DiscountStrategy, price: float):
        self.strategy = strategy
        self.price = price

    def give_discount(self) -> float:
        """Повертає суму знижки."""
        return self.strategy.get_discount(self.price)

    def get_final_price(self) -> float:
        """Повертає фінальну ціну після застосування знижки."""
        return self.price - self.give_discount()


# Приклад використання:
silver_discount = Discount(SilverDiscount(), 100)
print(f"Сума знижки (silver): {silver_discount.give_discount()}")  # 20.0
print(f"Фінальна ціна (silver): {silver_discount.get_final_price()}")  # 80.0

gold_discount = Discount(GoldDiscount(), 100)
print(f"Сума знижки (gold): {gold_discount.give_discount()}")  # 30.0
print(f"Фінальна ціна (gold): {gold_discount.get_final_price()}")  # 70.0

vip_discount = Discount(VIPDiscount(), 100)
print(f"Сума знижки (vip): {vip_discount.give_discount()}")  # 40.0
print(f"Фінальна ціна (vip): {vip_discount.get_final_price()}")  # 60.0