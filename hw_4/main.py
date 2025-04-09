from cv import generate_txt, cv
from fizzbuzz import generate_fizzbuzz_txt, fizzbuzz
from triangle_area import generate_area_txt, triangle_area

def main() -> None:
    """
    Prompts the user for their choice and generates the appropriate file.
    """
    user_choice: str = input("Enter 1 for CV file, 2 for FizzBuzz file, or 3 for Triangle area file: ")

    if user_choice == "1":
        generate_txt(cv)
    elif user_choice == "2":
        user_input: str = input("Enter a number or a comma-separated list: ")
        if ',' in user_input:
            numbers: list[int] = [int(i.strip()) for i in user_input.split(",")]
        else:
            numbers: int = int(user_input)

        generate_fizzbuzz_txt(fizzbuzz(numbers))
    elif user_choice == "3":
        try:
            a: float = float(input("Enter side a: "))
            b: float = float(input("Enter side b: "))
            c: float = float(input("Enter side c: "))
            result_type: str = input("Choose result type (int, float, str): ").strip().lower()

            if result_type not in {"int", "float", "str"}:
                raise ValueError("Invalid result type. Choose int, float, or str.")

        except ValueError as e:
            print("Input error:", e)
        else:
            result: float | int | str = triangle_area(a, b, c, result_type)
            print("Triangle area:", result)
            generate_area_txt(result)
        finally:
            print("Program execution finished.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()