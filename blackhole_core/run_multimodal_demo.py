import os
from data.multimodal.pdf_reader import extract_text_from_pdf
from data.multimodal.image_ocr import extract_text_from_image

# Base directory pointing to D:/Work_Station/data/multimodal
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "multimodal"))

def test_pdf_reader():
    print("📄 PDF Text Extraction Test")
    pdf_path = os.path.join(base_dir, "sample.pdf")
    print(f"Reading PDF from: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    print("Extracted Text:\n", text)
    print("-" * 50)

def test_image_ocr():
    print("🖼️ Image OCR Test")
    image_path = os.path.join(base_dir, "sample.jpg")
    print(f"Reading Image from: {image_path}")
    text = extract_text_from_image(image_path)
    print("Extracted Text:\n", text)
    print("-" * 50)

if __name__ == "__main__":
    test_pdf_reader()
    test_image_ocr()
