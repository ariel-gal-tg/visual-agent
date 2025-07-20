from PIL import ImageDraw
from PIL import Image
import os

def mark_coordinate_on_image(image_path, x, y, output_dir="screenshots_tests"):
    """
    Draws a red point at the given (x, y) coordinates on the image and saves it to the output directory.
    The output file is named after the element (spaces replaced with underscores).
    """
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    point_size = 2  # Adjust size for visibility
    draw.rectangle((x - point_size, y - point_size, x + point_size, y + point_size), fill="red")
    # Prepare output path
    output_path = os.path.join(output_dir, f"{x}_{y}_test.png")
    img.save(output_path)
    print(f"Marked screenshot saved to {output_path}")


def main():
    mark_coordinate_on_image("screenshot.png",1,2)
if __name__ == "__main__":
    main()