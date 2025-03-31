def fizzbuzz(numbers: int | list[int]) -> list[str]:
    """
    Генерує список значень FizzBuzz для чисел від 1 до numbers та списків.
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


user_input= input("Введіть число або список через кому: ")

if ',' in user_input:
    numbers = list(int(i.strip()) for i in user_input.split(","))
else:
    numbers = int(user_input)

print(fizzbuzz(numbers))