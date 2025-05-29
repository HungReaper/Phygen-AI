# PhyGen AI - AI-powered Physics Exam Generator

## 📝 Project Overview

PhyGen AI is an intelligent physics exam generator that uses optical character recognition (OCR) to analyze and extract text from physics-related images and documents. This tool is designed to help educators and students work with physics content effectively.

## 🚀 Features

- **OCR Integration**: Extract text from images and documents
- **Vietnamese & English Support**: Works with both Vietnamese and English text
- **RESTful API**: Simple API endpoints for easy integration
- **Scalable Architecture**: Built with FastAPI for high performance

## 🔧 Technology Stack

- **Backend**: Python, FastAPI
- **OCR Engine**: Tesseract OCR
- **Image Processing**: Pillow, pdf2image
- **Deployment**: Uvicorn

## 📋 Prerequisites

Before running this project, make sure you have:

1. **Python 3.8+** installed
2. **Tesseract OCR** installed:
   - Windows: Download and install from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - Make sure to include Vietnamese language data during installation
   - Default installation path: `C:\Program Files\Tesseract-OCR\tesseract.exe`

## 🛠️ Setup and Installation

### 1. Clone the repository

```powershell
git clone https://github.com/HungReaper/Phygen-AI.git
cd Phygen-AI
```

### 2. Create a virtual environment (Recommended)

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Running the application

```powershell
python -m app.main
```

The API will be available at `http://localhost:8000` or 'http://localhost:8000/doc#'

## 📚 API Reference

| Endpoint   | Method | Description                   | Request Body        | Response              |
|------------|--------|-------------------------------|--------------------|----------------------|
| `/`        | GET    | Welcome message               | None               | `{"message": "..."}`  |
| `/ocr/`    | POST   | Process image with OCR        | `file` (image)     | `{"text": "..."}`     |
| `/health/` | GET    | Health check for monitoring   | None               | `{"status": "..."}`   |

### Example API Usage (with curl):

```powershell
# Health check
curl http://localhost:8000/health/

# OCR processing (example using curl)
curl -X POST -F "file=@path/to/your/image.jpg" http://localhost:8000/ocr/
```

## 📁 Project Structure

```
Phygen-AI/
├── app/                      # Main application code
│   ├── main.py               # Entry point & app configuration
│   ├── api/                  # API routes
│   │   └── routes.py         # API endpoints
│   ├── ocr/                  # OCR processing modules
│   │   └── simple_ocr.py     # OCR implementation
│   └── utils/                # Utility functions
│       └── file_handlers.py  # File handling utilities
├── config/                   # Configuration
│   └── settings.py           # App settings
├── data/                     # Data directory
│   └── uploads/              # Temp storage for uploaded files
├── models/                   # AI models (if used)
├── tests/                    # Test files
├── requirements.txt          # Python dependencies
└── README.md                 # This documentation
```

## 💡 For C# Developers

If you're coming from a C# background, here are some key differences to note:

1. **Python vs C#**:
   - Python uses indentation for code blocks instead of curly braces `{}`
   - No type declarations needed in Python (but type hints are used in this project)
   - No semicolons to end statements

2. **FastAPI vs ASP.NET**:
   - FastAPI is similar to ASP.NET Core in concept
   - Route decorators (`@router.get("/")`) are like `[HttpGet]` attributes
   - Dependency injection exists but works differently

3. **Virtual Environment vs .NET SDK**:
   - Python's virtual environments are similar to project-specific .NET SDK installations
   - `requirements.txt` is similar to NuGet packages in your .csproj file

## 🤝 Contributing

1. Create a branch for your feature
2. Commit your changes with clear messages
3. Push your branch and create a pull request

## 📝 License

Copyright © 2023 Phygen-AI Team
