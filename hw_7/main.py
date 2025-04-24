from image_editor import (
    load_image,
    resize_image,
    save_image,
    analyze_image,
    save_analysis,
    apply_contour_pipeline
)

def main():
    image_name = 'img.pdf'
    image = load_image(image_name)

    resized = resize_image(image, (800, 600))
    processed = apply_contour_pipeline(resized)
    save_image(processed, 'processed_image.png')

    result = analyze_image(processed)
    save_analysis(result)

if __name__ == "__main__":
    main()