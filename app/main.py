from fastapi import FastAPI
from config.settings import settings
from app.api.routes import router

# Khởi tạo FastAPI
app = FastAPI(
    title="PhyGen",
    description="AI-powered Physics Exam Generator",
    version="0.1.0"
)

# Đăng ký router từ module routes
app.include_router(router)

# Chạy ứng dụng khi gọi trực tiếp file main.py
if __name__ == "__main__":
    import uvicorn
    # Sử dụng port 8000 và bật chế độ reload khi phát triển
    uvicorn.run("app.main:app", host=settings.API_HOST, port=settings.API_PORT, reload=settings.DEBUG)