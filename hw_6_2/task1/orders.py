class Order:
    """
    Ініціалізація класу Order з інформацією про замовлення.

    OOP: Інкапсуляція — поля зберігають деталі про замовлення.
    SOLID: SRP — обробляє лише одну сутність: замовлення.
    """
    def __init__(self, customer_info: dict):
        self.customer_surname = customer_info.get("customer_surname")
        self.product_name = customer_info.get("product_name")
        self.quantity = customer_info.get("quantity")
        self.price = customer_info.get("price")
        self.order_date = customer_info.get("date")

    def __str__(self):
        return f"Order by {self.customer_surname}, Product: {self.product_name}, Quantity: {self.quantity}, Total: {self.price * self.quantity}, Date: {self.order_date}"

class OrderSystem:
    """
    Клас для керування замовленнями клієнтів.

    OOP: Інкапсуляція — керує колекцією об'єктів Order.
    SOLID: SRP — відповідає лише за систему замовлень.
    """
    def __init__(self):
        self.orders = {}

    def add_order(self, order_number: int, order_info: dict):
        self.orders[order_number] = Order(order_info)

    def search_orders(self, **kwargs):
        return [order for order in self.orders.values() if all(getattr(order, k) == v for k, v in kwargs.items())]

    def remove_order(self, order_number: int):
        if order_number in self.orders:
            del self.orders[order_number]

    def get_order(self, order_number: int):
        return self.orders.get(order_number, "Замовлення не знайдено")

    def show_orders(self):
        for order in self.orders.values():
            print(order)