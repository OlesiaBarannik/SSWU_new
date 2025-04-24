from PIL import Image
from pdf2image import convert_from_path
import os

def load_image(filename):
    path = os.path.join("data", filename)
    if filename.lower().endswith('.pdf'):
        try:
            images = convert_from_path(path)
            image = images[0]  # беремо першу сторінку
            print(f"[INFO] PDF '{filename}' конвертовано в зображення")
            return image
        except Exception as e:
            print(f"[ERROR] Не вдалося конвертувати PDF: {e}")
            raise
    else:
        try:
            image = Image.open(path)
            print(f"[INFO] Зображення '{filename}' завантажено успішно")
            return image
        except FileNotFoundError:
            print(f"[ERROR] Зображення '{filename}' не знайдено за шляхом {path}")
            raise