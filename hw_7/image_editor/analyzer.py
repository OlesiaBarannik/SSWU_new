import os

def analyze_image(image):
    width, height = image.size
    result = f"Розмір зображення: {width}x{height}\n"
    result += "Це демонстраційний аналіз супутникового зображення.\n"
    print("[INFO] Аналіз завершено")
    return result

def save_analysis(result_text, filename="analysis.txt"):
    os.makedirs("results", exist_ok=True)
    path = os.path.join("results", filename)
    with open(path, "w") as f:
        f.write(result_text)
    print(f"[INFO] Аналіз збережено у: {path}")