import math

def triangle_area(a: float, b: float, c: float, result_type: str = "float"):
    """
    Calculates the area of a triangle using Heron's formula.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle sides"

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    if result_type == "int":
        return int(area)
    elif result_type == "str":
        return str(area)
    return area


def generate_area_txt(area: float) -> None:
    """
    Generates a triangle_area.txt file containing the calculated triangle area.
    """
    try:
        with open("triangle_area.txt", "w", encoding="utf-8") as file:
            file.write(f"Triangle area: {area}")
    except Exception as e:
        print(f"An error occurred while generating the .txt file: {e}")
    else:
        print("Triangle area was successfully saved as triangle_area.txt")
    finally:
        print("Generation process finished.")