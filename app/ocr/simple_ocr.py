from PIL import Image
import pytesseract
import io
import os
from pathlib import Path
import pdf2image
from typing import Union, List

# Import settings nếu cần
from config.settings import settings

def setup_tesseract():
    """Set up Tesseract path based on operating system"""
    if os.name == "nt":  # Windows
        tesseract_path = settings.TESSERACT_PATH
        if os.path.exists(tesseract_path):
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
    # Trên Linux/Mac không cần thiết lập đường dẫn nếu đã cài đặt qua package manager

def process_image(image: Image.Image, lang: str = "vie+eng") -> str:
    """Process a single image using Tesseract OCR
    
    Args:
        image: PIL Image object
        lang: OCR language(s)
        
    Returns:
        str: Extracted text
    """
    # Đảm bảo Tesseract được cấu hình đúng
    setup_tesseract()
    
    # Trích xuất văn bản
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()

def process_image_file(image_file, lang: str = "vie+eng") -> str:
    """Process an uploaded image file
    
    Args:
        image_file: UploadFile or bytes
        lang: OCR language(s)
        
    Returns:
        str: Extracted text
    """
    # Nếu là bytes, chuyển thành PIL Image
    if isinstance(image_file, bytes):
        image = Image.open(io.BytesIO(image_file))
    # Nếu là file-like object (như UploadFile.file)
    else:
        image = Image.open(image_file)
        
    return process_image(image, lang)

def process_pdf(pdf_path: Union[str, Path], lang: str = "vie+eng") -> List[str]:
    """Process a PDF file and extract text from each page
    
    Args:
        pdf_path: Path to PDF file
        lang: OCR language(s)
        
    Returns:
        List[str]: Extracted text from each page
    """
    # Chuyển PDF thành danh sách các hình ảnh
    images = pdf2image.convert_from_path(pdf_path)
    
    results = []
    # Xử lý từng trang
    for image in images:
        text = process_image(image, lang)
        results.append(text)
            
    return results