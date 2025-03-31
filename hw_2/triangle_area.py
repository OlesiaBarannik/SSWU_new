import math
def triangle_area(a: float, b: float, c: float, result_type: str = "float"):
    """
    Обчислює площу трикутника за формулою Герона
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "Некоректні сторони трикутника"

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    if result_type == "int":
        return int(area)
    elif result_type == "str":
        return str(area)
    return area  # За замовчуванням float

# Отримання вхідних даних від користувача
try:
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    c = float(input("Введіть сторону c: "))
    result_type = input("Оберіть тип результату (int, float, str): ").strip().lower()

    if result_type not in {"int", "float", "str"}:
        raise ValueError("Некоректний тип результату. Оберіть int, float або str.")

except ValueError as e:
    print("Помилка введення:", e)
else:
    result = triangle_area(a, b, c, result_type)
    print("Площа трикутника:", result)
finally:
    print("Завершення виконання програми.")