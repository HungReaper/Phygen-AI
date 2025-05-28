from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import io

from app.ocr.simple_ocr import process_image_file

router = APIRouter(
    tags=["OCR"],
    prefix="",
)

@router.get("/")
def root():
    return {"message": "Welcome to PhyGen OCR API"}

@router.post("/ocr/")
async def ocr_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        text = process_image_file(image_bytes)
        return JSONResponse(content={"text": text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")

@router.get("/health/")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "ok", "service": "PhyGen OCR"}