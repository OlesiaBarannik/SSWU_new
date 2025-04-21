import re
import requests
from bs4 import BeautifulSoup

class CVParser:
    """
    Клас для аналізу CV та пошуку позицій на основі ключових слів.

    OOP: Інкапсуляція — логіка пошуку прихована в методі.
    SOLID: SRP — єдина відповідальність: пошук ключових слів.
    """
    def __init__(self, cv_dict: dict):
        self.cv_dict = cv_dict

    def get_position_from_cv(self) -> list[str]:
        summary = self.cv_dict.get("summary", "")
        keywords = ["Junior Python Developer", "Trainee", "Junior Developer", "Junior"]
        return [kw for kw in keywords if re.search(rf"\b{re.escape(kw)}(?:[.,!?]|\s|$)", summary, re.IGNORECASE)]

class VacancyScraper:
    """
    Парсить вакансії з work.ua за ключовими словами.

    OOP: Інкапсуляція — реалізація логіки в методі scrape_filtered_vacancies.
    SOLID: SRP.
    """
    def __init__(self, keywords: list[str]):
        self.keywords = keywords
        self.url = "https://www.work.ua/jobs-python/"
        self.headers = {"User-Agent": "Chrome/112.0.0.0"}

    def scrape_filtered_vacancies(self) -> list[tuple[str, str]]:
        results = []
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Помилка при завантаженні сторінки: {e}")
            return []
        finally:
            print("Завершення парсингу вакансій.")

        soup = BeautifulSoup(response.text, "html.parser")
        for vacancy in soup.select("div.job-link"):
            try:
                a_tag = vacancy.find("h2").find("a")
                if a_tag:
                    title = a_tag.text.strip()
                    link = "https://www.work.ua" + a_tag["href"]
                    if any(re.search(rf"\b{re.escape(k)}\b", title, re.IGNORECASE) for k in self.keywords):
                        results.append((title, link))
            except AttributeError:
                continue
        return results

class VacancySaver:
    """
    Клас для збереження вакансій у текстовий файл.

    OOP: Інкапсуляція — логіка збереження прихована в методі.
    SOLID: SRP.
    """
    def __init__(self, vacancies: list[tuple[str, str]]):
        self.vacancies = vacancies

    @classmethod
    def from_scraper(cls, scraper: VacancyScraper):
        """
        Додано клас-метод — альтернатива створенню через об'єкт парсера.
        """
        return cls(scraper.scrape_filtered_vacancies())

    def save_to_txt(self, filename: str = "vacancies.txt") -> None:
        with open(filename, "w", encoding="utf-8") as file:
            for title, link in self.vacancies:
                file.write(f"{title}\n{link}\n\n")
