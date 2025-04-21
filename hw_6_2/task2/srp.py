class BankAccount:
    """Клас для зберігання даних про окремий банківський рахунок."""

    def __init__(self, account_no: str):
        self._account_no = account_no  # Номер рахунку (приватний атрибут)

    def get_account_number(self) -> str:
        """Повертає номер рахунку."""
        return self._account_no


class BankAccountManager:
    """Клас для управління списком банківських рахунків."""

    def __init__(self):
        self._accounts_list = []  # Список об'єктів BankAccount

    def save(self, account: BankAccount) -> None:
        """Зберігає об'єкт банківського рахунку до списку."""
        self._accounts_list.append(account)
        print(f"Account {account.get_account_number()} successfully saved to DB.")

    def get_all_accounts(self) -> list:
        """Повертає список номерів усіх збережених рахунків."""
        return [account.get_account_number() for account in self._accounts_list]


# Приклад використання:
manager = BankAccountManager()
acc1 = BankAccount("12345")
acc2 = BankAccount("67890")
manager.save(acc1)
manager.save(acc2)
print(manager.get_all_accounts())  # ['12345', '67890']