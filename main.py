import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import pyautogui
from PIL import ImageDraw

# Load environment variables from the .env file
load_dotenv()

def configure_api():
    """
    Configures the Google Generative AI API with the key from .env
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set GOOGLE_API_KEY in your .env file.")
    genai.configure(api_key=api_key)

def capture_screen():
    """
    Takes a screenshot and saves it to a file.
    Returns the path to the screenshot.
    """
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    return screenshot_path

def describe_image(image_path, prompt):
    """
    Sends an image and a prompt to the Gemini Vision model and gets a description.
    """
    print("Asking the vision model to describe the image...")
    # Initialize the specific model for vision
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Open the image file
    img = Image.open(image_path)
    
    # Generate content
    # The model can take a list of parts, including text prompts and images
    response = model.generate_content([prompt, img])
    
    return response.text

def mark_coordinate_on_image(image_path, coords, element_name, output_dir="screenshots_output"):
    """
    Draws a red circle at the given coordinates on the image and saves it to the output directory.
    The output file is named after the element (spaces replaced with underscores).
    """
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    try:
        x, y = map(int, coords.split(","))
    except Exception:
        print(f"Could not parse coordinates: {coords}")
        return
    radius = 10
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill="red", outline="red")
    # Prepare output path
    safe_name = element_name.replace(" ", "_")
    output_path = os.path.join(output_dir, f"{safe_name}.png")
    img.save(output_path)
    print(f"Marked screenshot saved to {output_path}")

def main():
    """
    Main function to run the visual agent MVP.
    """
    try:
        # 1. Set up the API
        configure_api()
        
        # 2. Capture the current screen
        screenshot_file = capture_screen()
        
        # 3. Define what we want to ask about the image
        prompt = "Describe exactly what you see on this computer screen. Be detailed about open windows, icons, and any text you can read."
        
        # 4. Get the description from the model
        description = describe_image(screenshot_file, prompt)
        
        # 5. Print the result
        print("\n--- Vision Model Output ---")
        print(description)
        print("---------------------------\n")

        # 6. Print screen resolution
        screen_width, screen_height = pyautogui.size()
        print(f"Screen resolution: {screen_width}x{screen_height}")

        # 7. Ask user what to click
        element = input("What do you want to click on? (e.g., 'Save button'): ")

        # 8. Ask Gemini for coordinates
        coord_prompt = f"Given this screenshot, and the fact is in {screen_width}x{screen_height} screen resolution, what are the (x, y) pixel coordinates of the center of the '{element}'? Respond with only the coordinates as two integers separated by a comma."
        coords = describe_image(screenshot_file, coord_prompt)
        print(f"Coordinates for '{element}': {coords}")

        # 9. Mark the coordinate on the screenshot and save it
        mark_coordinate_on_image(screenshot_file, coords, element)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()