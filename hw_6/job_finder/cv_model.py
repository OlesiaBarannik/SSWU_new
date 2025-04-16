class CV:
    def __init__(self, cv_data: dict):
        """
        Ініціалізація класу CV, приймає словник cv_data з даними для резюме.
        """
        self._cv_data = cv_data  # Зберігаємо дані для резюме

    def generate_cv(self) -> str:
        """
        Генерує текст резюме на основі переданих даних.
        """
        contact = f"Name: {self._cv_data['personal_info']['name']}\n"
        contact += f"Region: {self._cv_data['personal_info']['region']}\n"
        contact += f"Email: {self._cv_data['personal_info']['email']}\n"
        contact += f"Phone: {self._cv_data['personal_info']['phone']}\n"

        summary = f"\nSummary:\n{self._cv_data['summary']}"

        skills = "\nSkills:\n"
        for category, values in self._cv_data["skills"].items():
            skills += f"{category}: {', '.join(values)}\n"

        experience = "\nExperience:\n"
        for exp in self._cv_data["experience"]:
            experience += f"{exp['position']} at {exp['company']} ({exp['period']}):\n"
            experience += "\n".join([f"- {task}" for task in exp['tasks']]) + "\n"

        education = f"\nEducation:\n{self._cv_data['education']['degree']}, {self._cv_data['education']['university']} ({self._cv_data['education']['graduation_year']})"

        courses = "\nCourses and Certificates:\n"
        for org, title, period in self._cv_data["courses_certificates"]:
            courses += f"{org}: {title} ({period})\n"

        projects = "\nProjects:\n"
        for project in self._cv_data["projects"]:
            projects += f"{project['name']}:\n{project['description']}\n"
            projects += "\n".join([f"- {task}" for task in project["tasks"]]) + "\n"

        # Формуємо текстове резюме
        full_cv = f"{contact}{summary}{skills}{experience}{education}{courses}{projects}"

        return full_cv

class CVFileSaver:
    def __init__(self, cv_object: CV):
        """
        Ініціалізація класу для збереження резюме у файл.
        Приймає об'єкт класу CV.
        """
        self.cv_object = cv_object

    def save_to_file(self, filename: str):
        """
        Зберігає сформоване резюме в текстовий файл.
        """
        cv_text = self.cv_object.generate_cv()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cv_text)
        print(f"Резюме збережено в файл: {filename}")