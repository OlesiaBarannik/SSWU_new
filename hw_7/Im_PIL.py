import random
from PIL import Image, ImageDraw
from PIL.ImageFilter import CONTOUR

# --------------------- зчитування файлу зображення ----------------------
def image_read(file_name: str):
    """Функція для відкриття зображення та повернення його інформації."""
    image = Image.open(file_name)
    draw = ImageDraw.Draw(image)
    pixels = image.load()
    width, height = image.size
    return image, draw, pixels, width, height

# --------------------- відтінки сірого ----------------------
def shades_of_gray(file_name_start: str, file_name_stop: str):
    """Застосування відтінків сірого до зображення."""
    image, draw, pixels, width, height = image_read(file_name_start)

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            avg = (r + g + b) // 3  # Усереднення пікселів
            pixels[i, j] = (avg, avg, avg)

    image.save(file_name_stop, "JPEG")  # Збереження після обробки
    print(f'[INFO] Збережено після застосування відтінків сірого: {file_name_stop}')


# ------------------------- серпія --------------------------
def serpia(file_name_start: str, file_name_stop: str, depth=30):
    """Застосування серпії до зображення."""
    image, draw, pixels, width, height = image_read(file_name_start)

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            S = (r + g + b) // 3
            r = min(255, S + depth * 2)
            g = min(255, S + depth)
            b = min(255, S)
            pixels[i, j] = (r, g, b)

    image.save(file_name_stop, "JPEG")
    print(f'[INFO] Збережено після застосування серпії: {file_name_stop}')


# ----------------------- негатив --------------------------
def negative(file_name_start: str, file_name_stop: str):
    """Застосування негативу до зображення."""
    image, draw, pixels, width, height = image_read(file_name_start)

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    image.save(file_name_stop, "JPEG")
    print(f'[INFO] Збережено після застосування негативу: {file_name_stop}')


# ----------------------- зашумлення ------------------------
def noise(file_name_start: str, file_name_stop: str, factor=30):
    """Додавання шуму до зображення."""
    image, draw, pixels, width, height = image_read(file_name_start)

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            rand = random.randint(-factor, factor)
            r = min(255, max(0, r + rand))
            g = min(255, max(0, g + rand))
            b = min(255, max(0, b + rand))
            pixels[i, j] = (r, g, b)

    image.save(file_name_stop, "JPEG")
    print(f'[INFO] Збережено після додавання шуму: {file_name_stop}')


# ---------------------- зміна яскравості --------------------
def brightness_change(file_name_start: str, file_name_stop: str, factor=50):
    """Зміна яскравості зображення."""
    image, draw, pixels, width, height = image_read(file_name_start)

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = min(255, max(0, r + factor))
            g = min(255, max(0, g + factor))
            b = min(255, max(0, b + factor))
            pixels[i, j] = (r, g, b)

    image.save(file_name_stop, "JPEG")
    print(f'[INFO] Збережено після зміни яскравості: {file_name_stop}')


# --------------------------- монохромне зображення ------------------------
def monochrome(file_name_start: str, file_name_stop: str, factor=50):
    """Перетворення зображення в монохромне."""
    image, draw, pixels, width, height = image_read(file_name_start)

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            S = r + g + b
            if S > (((255 + factor) // 2) * 3):
                r, g, b = 255, 255, 255
            else:
                r, g, b = 0, 0, 0
            pixels[i, j] = (r, g, b)

    image.save(file_name_stop, "JPEG")
    print(f'[INFO] Збережено після монохромного перетворення: {file_name_stop}')


# ------------------ фільтрація - векторизація зображення ------------------------
def contour_im(file_name_start: str, file_name_stop: str):
    """Застосування контуру до зображення."""
    image, draw, pixels, width, height = image_read(file_name_start)

    # Застосування фільтра контуру
    image_filter = image.filter(CONTOUR)
    image_filter.save(file_name_stop, "JPEG")
    print(f'[INFO] Збережено після застосування контуру: {file_name_stop}')
