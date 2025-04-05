import numpy as np
import json

cv = {
    "personal_info": {# dict
        "name": "Olesia Barannik",
        "region": "Kyiv",
        "email": "olesyabarannik23@gmail.com",
        "phone": "+38 (093) 966 46 81",
    },
    "summary": (
        "I am seeking an entry-level position as a Junior Python Developer or Trainee. "
        "I possess a strong interest in programming and a willingness to learn and grow within a dynamic organization."
    ),
    "skills": {
        "Programming": {"Python", "Django", "Django REST Framework", "JavaScript", "HTML", "CSS"},  # set
        "Databases": {"PostgreSQL", "MongoDB"},  # set
        "Tools": {"Git", "PyCharm", "Docker"},  # set
        "Data Analysis": {"Big Data Analysis", "MS Excel"},  # set
        "Languages": {"English: Intermediate"}  # set
    },
    "experience": [  # list
        {
            "position": "Project Forum Participant",
            "company": "SoftServe",
            "period": "2024.06 - 2024.12",
            "tasks": ["Bug fixing and functionality improvement"]  # list
        },
        {
            "position": "Financial Analyst",
            "company": "SaVService",
            "period": "2019 - 2023",
            "tasks": [  # list
                "Investment analysis of counteragents",
                "Calculation of financial indicators in contracts",
                "Pricing strategy and cost analysis",
                "Marketing fund planning and control",
                "Quarterly financial reporting and adjustments"
            ]
        }
    ],
    "education": {
        "university": "Kyiv National University of Trade and Economics",
        "degree": "Master in Finance and Banking",
        "graduation_year": 2013
    },
    "courses_certificates": [  # list
        ("SoftServe", "Complete Python Developer Course", "2023.05 - 2024.05"),  # tuple
        ("Beetroot Academy", "Python", "2023"),  # tuple
        ("Perspectiva", "MS SQL", "2021"),  # tuple
        ("Laba", "Financial Modeling", "2021"),  # tuple
        ("Danko Training Center", "MS Excel (Professional Level)", "2019")  # tuple
    ],
    "projects": np.array([  # array
        {
            "name": "Forum",
            "description": (
                "WebAPI application to connect startups with investors, developed using Django REST Framework."
            ),
            "tasks": [
                "Implemented user Sign In with JWT and added specific user data",
                "Created, updated, and validated startup profiles",
                "Set up WebSocket for direct communication",
                "Implemented notifications for incoming messages",
                "Created an industries table and populated it using loaddata"
            ]
        },
        {
            "name": "Telegram bot for medication intake",
            "description": (
                "A bot reminding users to take their medications at the specified time, supporting multiple medications."
            ),
            "tasks": [
                "Created a bot using the python-telegram-bot library",
                "Configured medication reminders",
                "Managed multiple medication schedules"
            ]
        }
    ])
}

def generate_txt(cv):
    try:
        with open("cv.txt", "w",  encoding="utf-8") as file:
            file.write(f"Name: {cv['personal_info']['name']}\n")
            file.write(f"Region: {cv['personal_info']['region']}\n")
            file.write(f"Email: {cv['personal_info']['email']}\n")
            file.write(f"Phone: {cv['personal_info']['phone']}\n")

            file.write("Summary:\n")
            file.write(f"{cv['summary']}\n\n")

            file.write("Skills:\n")
            for category, skills in cv['skills'].items():
                file.write(f"{category}: {','.join(skills)}\n")

            file.write("Experience:\n")
            for exp in cv['experience']:
                file.write(f"{exp['position']} at {exp['company']} ({exp['period']})\n")
                for task in exp['tasks']:
                    file.write(f"  - {task}\n")
            file.write("\n")

            file.write("Education:\n")
            file.write(f"{cv['education']['university']}, {cv['education']['degree']} (Graduation Year: {cv['education']['graduation_year']})\n\n")

            file.write("Courses & Certificates:\n")
            for course in cv['courses_certificates']:
                file.write(f"  - {course[0]} - {course[1]} ({course[2]})\n")
            file.write("\n")

            file.write("Projects:\n")
            for project in cv['projects']:
                file.write(f"Project: {project['name']}\n")
                file.write(f"Description: {project['description']}\n")
                file.write("Tasks:\n")
                for task in project['tasks']:
                    file.write(f"  - {task}\n")
                file.write("\n")

    except Exception as e:
        print(f"An error occurred while generating the .txt file: {e}")
    else:
        print("CV was successfully saved as CV.txt")
    finally:
        print("Generation process finished.")


def generate_json(cv):
    try:
        serializable_cv = make_json_serializable(cv)
        with open("CV.json", "w", encoding="utf-8") as file:
            json.dump(serializable_cv, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"An error occurred while generating the .json file: {e}")
    else:
        print("CV was successfully saved as CV.json")
    finally:
        print("Generation process finished.")


def make_json_serializable(data):
    if isinstance(data, dict):
        return {key: make_json_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [make_json_serializable(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(make_json_serializable(item) for item in data)
    elif isinstance(data, set):
        return [make_json_serializable(item) for item in data]  # set у список
    elif isinstance(data, np.ndarray):
        return make_json_serializable(data.tolist())  # array → list → обробка
    else:
        return data

def generate_file(cv):
    file_type = input("Enter the file format ('txt' or 'json'): ").strip().lower()

    match file_type:
        case 'txt':
            generate_txt(cv)
        case 'json':
            generate_json(cv)
        case _:
            print("Invalid file type. Please choose either 'txt' or 'json'.")

if __name__ == "__main__":
    generate_file(cv)