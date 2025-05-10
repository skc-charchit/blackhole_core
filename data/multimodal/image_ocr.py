import pytesseract
from PIL import Image

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    print(f"Image format: {image.format}")
    text = pytesseract.image_to_string(image)
    return text
