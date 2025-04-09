def fizzbuzz(numbers: int | list[int]) -> list[str]:
    """
    Generates a list of FizzBuzz values for numbers from 1 to the given number or for a list of numbers.
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
    Generates a fizzbuzz.txt file containing the FizzBuzz output.
    """
    try:
        with open("fizzbuzz.txt", "w",encoding="utf-8") as file:
            file.write(f"FizzBuzz Output:\n{', '.join(fizzbuzz_result)}")
    except Exception as e:
        print(f"An error occurred while generating the .txt file: {e}")
    else:
        print("FizzBuzz was successfully saved as fizzbuzz.txt")
    finally:
        print("Generation process finished.")
