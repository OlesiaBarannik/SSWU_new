from job_finder import cv, get_position_from_cv, scrape_filtered_vacancies, save_vacancies_to_txt
from fizzbuzz import generate_fizzbuzz_txt, fizzbuzz
from triangle_area import generate_area_txt, triangle_area


def main() -> None:
    """
    Запитує вибір користувача та генерує відповідний файл.
    """
    try:
        user_choice: str = input(
            "Введіть 1 для файлу з вакансіями, 2 для файлу FizzBuzz або 3 для файлу з площею трикутника: ")

        if user_choice == "1":
            keywords_from_cv = get_position_from_cv(cv)

            if not keywords_from_cv:
                print("Не знайдено відповідних ключових слів у CV.")
                return

            vacancies = scrape_filtered_vacancies(keywords_from_cv)

            if not vacancies:
                print("Не знайдено вакансій за ключовими словами.")
            else:
                save_vacancies_to_txt(vacancies)
                print(f"Знайдено та збережено {len(vacancies)} вакансій у файл vacancies.txt")

        elif user_choice == "2":
            user_input: str = input("Введіть число або список чисел через кому: ")
            if ',' in user_input:
                numbers: list[int] = [int(i.strip()) for i in user_input.split(",")]
            else:
                numbers: int = int(user_input)

            generate_fizzbuzz_txt(fizzbuzz(numbers))

        elif user_choice == "3":
            try:
                a: float = float(input("Введіть сторону a: "))
                b: float = float(input("Введіть сторону b: "))
                c: float = float(input("Введіть сторону c: "))
                result_type: str = input("Оберіть тип результату (int, float, str): ").strip().lower()

                if result_type not in {"int", "float", "str"}:
                    raise ValueError("Неправильний тип результату. Оберіть int, float або str.")

            except ValueError as e:
                print("Помилка вводу:", e)
            else:
                result: float | int | str = triangle_area(a, b, c, result_type)
                print("Площа трикутника:", result)
                generate_area_txt(result)

        else:
            print("Невірний вибір. Введіть 1, 2 або 3.")

    finally:
        print("Завершення виконання програми.")

if __name__ == "__main__":
    main()