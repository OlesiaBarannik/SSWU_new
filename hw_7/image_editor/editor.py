import os
from PIL import Image, ImageFilter

# Розмір зображення
def resize_image(image, size=(800, 600)):
    """Функція для зміни розміру зображення"""
    resized = image.resize(size)
    print(f"[INFO] Зображення змінено до розміру {size}")
    return resized

# Збереження зображення
def save_image(image, filename):
    """Функція для збереження зображення у вказаний файл"""
    os.makedirs("results", exist_ok=True)
    path = os.path.join("results", filename)
    image.save(path)
    print(f"[INFO] Зображення збережено за шляхом: {path}")

# Перетворення в відтінки сірого
def apply_shades_of_gray(image):
    """Функція для застосування відтінків сірого до зображення"""
    print("[INFO] Застосування shades_of_gray()")
    image = image.convert("RGB")
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            avg = (r + g + b) // 3
            pixels[x, y] = (avg, avg, avg)
    return image

# Перетворення в монохромне зображення
def apply_monochrome(image, factor=80):
    """Функція для застосування монохромного фільтра"""
    print(f"[INFO] Застосування monochrome() з factor={factor}")
    image = image.convert("RGB")
    pixels = image.load()
    width, height = image.size
    threshold = ((255 + factor) // 2) * 3
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            S = r + g + b
            if S > threshold:
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
    return image

# Застосування фільтру контуру
def apply_contour(image):
    """Функція для застосування фільтру контуру до зображення"""
    print("[INFO] Застосування фільтру контуру")
    return image.filter(ImageFilter.CONTOUR)

# Обробка зображення (відтінки сірого -> монохром -> контур)
def apply_contour_pipeline(image, factor=80):
    """Функція для поетапного застосування фільтрів: відтінки сірого -> монохром -> контур"""
    print("[INFO] Старт контурного пайплайну (shades_of_gray ➝ monochrome ➝ contour)")
    image = apply_shades_of_gray(image)
    image = apply_monochrome(image, factor)
    image = apply_contour(image)
    return image
