import math

def triangle_area(a: float, b: float, c: float, result_type: str = "float"):
    """
    Обчислює площу трикутника за формулою Герона.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "Неприпустимі сторони трикутника"

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    if result_type == "int":
        return int(area)
    elif result_type == "str":
        return str(area)
    return area


def generate_area_txt(area: float) -> None:
    """
    Створює файл triangle_area.txt, який містить обчислену площу трикутника.
    """
    try:
        with open("triangle_area.txt", "w", encoding="utf-8") as file:
            file.write(f"Площа трикутника: {area}")
    except Exception as e:
        print(f"Сталася помилка під час створення .txt файлу: {e}")
    else:
        print("Площа трикутника успішно збережена у файл triangle_area.txt")
    finally:
        print("Процес генерації завершено.")