class CV:
    """
    Ініціалізація класу CV, приймає словник cv_data з даними для резюме.

    OOP: Інкапсуляція — дані приховані у _cv_data.
    SOLID: SRP — клас відповідає лише за генерацію текстового резюме.
    """
    def __init__(self, cv_data: dict):
        self._cv_data = cv_data

    def generate_cv(self) -> str:
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

        return f"{contact}{summary}{skills}{experience}{education}{courses}{projects}"

class CVFileSaver:
    """
    Ініціалізація класу для збереження резюме у файл.

    OOP: Інкапсуляція — взаємодія з CV через метод.
    SOLID: SRP — відповідає лише за збереження файлу.
    """
    def __init__(self, cv_object: CV):
        self.cv_object = cv_object

    def save_to_file(self, filename: str):
        cv_text = self.cv_object.generate_cv()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cv_text)
        print(f"Резюме збережено в файл: {filename}")