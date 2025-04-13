def fizzbuzz(numbers: int | list[int]) -> list[str]:
    """
    Генерує список значень FizzBuzz для чисел від 1 до заданого числа або для списку чисел.
    """
    result: list[str] = []
    if isinstance(numbers, int):
        numbers = range(1, numbers + 1)

    for n in numbers:
        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))
    return result

def generate_fizzbuzz_txt(fizzbuzz_result: list[str]) -> None:
    """
    Створює файл fizzbuzz.txt, що містить результат виконання FizzBuzz.
    """
    try:
        with open("fizzbuzz.txt", "w", encoding="utf-8") as file:
            file.write(f"Результат FizzBuzz:\n{', '.join(fizzbuzz_result)}")
    except Exception as e:
        print(f"Сталася помилка під час створення .txt файлу: {e}")
    else:
        print("FizzBuzz успішно збережено у файл fizzbuzz.txt")
    finally:
        print("Процес генерації завершено.")