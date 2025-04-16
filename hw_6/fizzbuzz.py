class FizzBuzzGenerator:
    """
    Генерує список значень FizzBuzz для чисел від 1 до заданого числа або для списку чисел.
    """

    def __init__(self, numbers: int | list[int]):
        self.result: list[str] = []
        if isinstance(numbers, int):
            self.numbers = range(1, numbers + 1)
        else:
            self.numbers = numbers

    def generate(self) -> list[str]:
        for n in self.numbers:
            if n % 3 == 0 and n % 5 == 0:
                self.result.append("FizzBuzz")
            elif n % 3 == 0:
                self.result.append("Fizz")
            elif n % 5 == 0:
                self.result.append("Buzz")
            else:
                self.result.append(str(n))
        return self.result


class FileSaver:
    """
    Зберігає передані дані у файл.
    """

    @staticmethod
    def save_to_txt(filename: str, data: list[str]) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Результат FizzBuzz:\n{', '.join(data)}")
        except Exception as e:
            print(f"Сталася помилка під час створення .txt файлу: {e}")
        else:
            print(f"FizzBuzz успішно збережено у файл {filename}")
        finally:
            print("Процес генерації завершено.")
