import re
import requests
from bs4 import BeautifulSoup

class CVParser:
    def __init__(self, cv_dict: dict):
        """
        Ініціалізуємо клас CVParser, який працює з даними резюме.
        """
        self.cv_dict = cv_dict

    def get_position_from_cv(self) -> list[str]:
        """
        Отримує список позицій з резюме на основі ключових слів.
        """
        summary = self.cv_dict.get("summary", "")
        keywords = ["Junior Python Developer", "Trainee", "Junior Developer", "Junior"]
        found_positions = []

        for keyword in keywords:
            pattern = rf"\b{re.escape(keyword)}(?:[.,!?]|\s|$)"
            if re.search(pattern, summary, re.IGNORECASE):
                found_positions.append(keyword)
        return found_positions


class VacancyScraper:
    def __init__(self, keywords: list[str]):
        """
        Ініціалізуємо клас VacancyScraper, який здійснює парсинг вакансій за ключовими словами.
        """
        self.keywords = keywords
        self.url = "https://www.work.ua/jobs-python/"
        self.headers = {"User-Agent": "Chrome/112.0.0.0"}

    def scrape_filtered_vacancies(self) -> list[tuple[str, str]]:
        """Парсить вакансії з сайту work.ua за ключовими словами."""
        results = []
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Викидає виключення, якщо статус код не 200
        except requests.exceptions.RequestException as e:
            print(f"Помилка при завантаженні сторінки: {e}")
            return []
        finally:
            print("Завершення парсингу вакансій.")

        soup = BeautifulSoup(response.text, "html.parser")
        vacancies = soup.select("div.job-link")

        for vacancy in vacancies:
            try:
                a_tag = vacancy.find("h2").find("a")
                if a_tag:
                    title = a_tag.text.strip()
                    link = "https://www.work.ua" + a_tag["href"]
                    # Фільтруємо вакансії по ключовим словам
                    for keyword in self.keywords:
                        if re.search(rf"\b{re.escape(keyword)}\b", title, re.IGNORECASE):
                            results.append((title, link))
                            break  # щоб не показувало одну вакансію декілька разів
            except AttributeError:
                # Якщо виникає помилка при пошуку елемента, продовжуємо
                continue
        return results


class VacancySaver:
    def __init__(self, vacancies: list[tuple[str, str]]):
        """
        Ініціалізуємо клас VacancySaver, який зберігає вакансії в текстовий файл.
        """
        self.vacancies = vacancies

    def save_to_txt(self, filename: str = "vacancies.txt") -> None:
        """Зберігає вакансії у текстовий файл."""
        with open(filename, "w", encoding="utf-8") as file:
            for title, link in self.vacancies:
                file.write(f"{title}\n{link}\n\n")
