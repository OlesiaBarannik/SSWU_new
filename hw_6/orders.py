class Order:
    def __init__(self, customer_info: dict):
        """
        Ініціалізація класу Order з інформацією про замовлення.
        """
        self.customer_surname = customer_info.get("customer_surname")
        self.product_name = customer_info.get("product_name")
        self.quantity = customer_info.get("quantity")
        self.price = customer_info.get("price")
        self.order_date = customer_info.get("date")

    def __str__(self):
        return f"Order by {self.customer_surname}, Product: {self.product_name}, Quantity: {self.quantity}, Total: {self.price * self.quantity}, Date: {self.order_date}"


class OrderSystem:
    def __init__(self):
        self.orders = {}

    def add_order(self, order_number: int, order_info: dict):
        """
        Додає нове замовлення в систему.
        """
        order = Order(order_info)  # Створюємо об'єкт Order з переданого словника
        self.orders[order_number] = order

    def search_orders(self, **kwargs):
        """
        Шукає замовлення за переданими параметрами (наприклад, за прізвищем клієнта, товаром, датою замовлення).
        """
        found_orders = []
        for order in self.orders.values():
            if all(getattr(order, key) == value for key, value in kwargs.items()):
                found_orders.append(order)
        return found_orders

    def remove_order(self, order_number: int):
        """
        Видаляє замовлення за його порядковим номером.
        """
        if order_number in self.orders:
            del self.orders[order_number]

    def get_order(self, order_number: int):
        """
        Повертає замовлення за його порядковим номером.
        """
        return self.orders.get(order_number, "Замовлення не знайдено")

    def show_orders(self):
        """
        Виводить всі замовлення.
        """
        for order in self.orders.values():
            print(order)


