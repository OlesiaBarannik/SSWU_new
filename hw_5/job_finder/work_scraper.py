import re
import requests
from bs4 import BeautifulSoup

def get_position_from_cv(cv_dict: dict) -> list[str]:
    """Отримує список позицій з резюме на основі ключових слів."""
    summary = cv_dict.get("summary", "")

    keywords = ["Junior Python Developer", "Trainee", "Junior Developer", "Junior"]
    found_positions = []

    for keyword in keywords:
        pattern = rf"\b{re.escape(keyword)}(?:[.,!?]|\s|$)"
        if re.search(pattern, summary, re.IGNORECASE):
            found_positions.append(keyword)
    return found_positions

def scrape_filtered_vacancies(keywords: list[str]) -> None:
    """Парсить вакансії з сайту work.ua за ключовими словами."""
    url = "https://www.work.ua/jobs-python/"
    headers = {"User-Agent": "Chrome/112.0.0.0"}
    results = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Викидає виключення, якщо статус код не 200
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return
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
                for keyword in keywords:
                    if re.search(rf"\b{re.escape(keyword)}\b", title, re.IGNORECASE):
                        results.append((title, link))
                        break  # щоб не показувало одну вакансію декілька разів
        except AttributeError:
            # Якщо виникає помилка при пошуку елемента, продовжуємо
            continue
    return results


def save_vacancies_to_txt(vacancies: list[tuple[str, str]], filename: str = "vacancies.txt") -> None:
    """Зберігає вакансії у текстовий файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for title, link in vacancies:
            file.write(f"{title}\n{link}\n\n")
