from job_finder import cv, CVParser, VacancyScraper, VacancySaver
from fizzbuzz import FizzBuzzGenerator, FileSaver
from area import Triangle, Rectangle, AreaWriter
from job_finder import CV, CVFileSaver
from library import Library
from orders import OrderSystem

def main() -> None:
    """
    Запитує вибір користувача та генерує відповідний файл.
    """
    try:
        user_choice: str = input(
            "Введіть 1 для файлу з вакансіями, 2 для файлу FizzBuzz, 3 для файлу з площею фігури, 4 для формування резюме, 5 для роботи з бібліотекою, 6 для роботи з інтернет-замовленнями: "
        )

        if user_choice == "1":
            cv_parser = CVParser(cv)
            keywords_from_cv = cv_parser.get_position_from_cv()

            if not keywords_from_cv:
                print("Не знайдено відповідних ключових слів у CV.")
                return

            vacancy_scraper = VacancyScraper(keywords_from_cv)
            vacancy_saver = VacancySaver.from_scraper(vacancy_scraper)
            if not vacancy_saver.vacancies:
                print("Не знайдено вакансій за ключовими словами.")
            else:
                vacancy_saver.save_to_txt("vacancies.txt")
                print(f"Знайдено та збережено {len(vacancy_saver.vacancies)} вакансій у файл vacancies.txt")

        elif user_choice == "2":
            user_input: str = input("Введіть число або список чисел через кому: ")
            if ',' in user_input:
                numbers: list[int] = [int(i.strip()) for i in user_input.split(",")]
            else:
                numbers: int = int(user_input)

            fizzbuzz_generator = FizzBuzzGenerator(numbers)
            result = fizzbuzz_generator.generate()

            file_saver = FileSaver()
            file_saver.save_to_txt("fizzbuzz.txt", result)

        elif user_choice == "3":
            shape_choice: str = input("Оберіть фігуру для обчислення площі (1 для трикутника, 2 для прямокутника): ")

            if shape_choice == "1":
                a: float = float(input("Введіть сторону a: "))
                b: float = float(input("Введіть сторону b: "))
                c: float = float(input("Введіть сторону c: "))
                result_type: str = input("Оберіть тип результату (int, float, str): ").strip().lower()

                triangle = Triangle(a, b, c)
                result = triangle.area(result_type)

                print("Площа трикутника:", result)
                area_writer = AreaWriter("Triangle", result)
                area_writer.to_txt()

            elif shape_choice == "2":
                width: float = float(input("Введіть ширину прямокутника: "))
                height: float = float(input("Введіть висоту прямокутника: "))
                result_type: str = input("Оберіть тип результату (int, float, str): ").strip().lower()

                rectangle = Rectangle(width, height)
                result = rectangle.area(result_type)

                print("Площа прямокутника:", result)
                area_writer = AreaWriter("Rectangle", result)
                area_writer.to_txt()

            else:
                print("Невірний вибір фігури.")

        elif user_choice == "4":
            cv_object = CV(cv)
            cv_saver = CVFileSaver(cv_object)
            cv_saver.save_to_file("resume.txt")
            print("Резюме успішно сформовано та збережено у файл resume.txt")

        elif user_choice == "5":
            library = Library()
            library.add_book(1, {
                "author": "J.K. Rowling",
                "title": "Harry Potter",
                "publisher": "Bloomsbury",
                "genre": "Fantasy",
                "year": 1997
            })
            library.add_book(2, {
                "author": "J.R.R. Tolkien",
                "title": "The Hobbit",
                "publisher": "HarperCollins",
                "genre": "Fantasy",
                "year": 1937
            })
            library.show_books()

        elif user_choice == "6":
            order_system = OrderSystem()
            order_system.add_order(1, {
                "customer_surname": "Ivanenko",
                "product_name": "Laptop",
                "quantity": 1,
                "price": 1500,
                "date": "2023-04-15"
            })
            order_system.add_order(2, {
                "customer_surname": "Petrenko",
                "product_name": "Smartphone",
                "quantity": 2,
                "price": 800,
                "date": "2023-04-16"
            })
            order_system.show_orders()

        else:
            print("Невірний вибір. Введіть число від 1 до 6.")

    finally:
        print("Завершення виконання програми.")

if __name__ == "__main__":
    main()