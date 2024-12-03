
# Learning Platform with Simulated Cloud Services

## Prerequisites

Before running this project locally, ensure you have Python installed on your system. Follow the steps below:

### 1. Check if Python is Installed

Open your command prompt (CMD) and enter the following command:

```bash
python --version
```

- If Python is installed, you will see something like this in your command prompt (your Python version may vary):

  ![Python Download](https://github.com/user-attachments/assets/832a8ee0-24ba-4c46-a296-be21912a5f3e)

- If you get an error or a different message, it means Python is not installed. In that case, download and install Python from the official [Python website](https://www.python.org/downloads/).

 ![image](https://github.com/user-attachments/assets/67291d31-10b4-4e4e-9027-1a3d3bb57259)

### 2. Install Dependencies

Once Python is set up, navigate to the project directory and install the required dependencies:

```bash
pip install -r requirements.txt
```
### Dependencies

This project requires the following Python packages:

- **Flask** - A lightweight WSGI web application framework.
- **python-dotenv** - A tool to read key-value pairs from `.env` file into environment variables.
- **Werkzeug** - A comprehensive WSGI web application library that Flask is built on.
- **typing-extensions** - Backport of the latest typing features from Python 3.10 and beyond.
- **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask for easy database integration.
- **Flask-Login** - Provides session management for Flask applications.
- **Jinja2** - A templating engine for Python, used by Flask to render HTML.
A Flask-based learning platform that simulates cloud services for course management, job searching, and CV generation.

## Features

### Course Management
- Browse available courses
- Detailed course information and modules
- Interactive quizzes for each course
- Track learning progress

### Job Board
- View available tech jobs
- Filter jobs by skills
- Detailed job descriptions and requirements
- Easy application process

### CV Builder
- AI-assisted CV generation
- Skills-based recommendations
- Professional CV templates
- Download and share options

### Cloud Service Simulations
- **Storage Service (OBS)**: File upload/download functionality
- **AI Service (ModelArts)**: CV generation and job recommendations
- **Elastic Cloud Server (ECS)**: Scalable web application hosting

## Project Structure

```
project/
├── api/                    # API endpoints
│   └── index.py           # Main API entry point
├── models/                 # Data models
│   ├── course.py          # Course-related models
│   ├── job.py             # Job-related models
│   └── quiz.py            # Quiz-related models
├── routes/                 # Route handlers
│   ├── ai_models.py       # AI service routes
│   ├── storage.py         # Storage service routes
│   └── views.py           # Main view routes
├── services/              # Business logic
│   ├── ai_service.py      # AI-related services
│   └── storage_service.py # Storage-related services
├── static/                # Static assets
├── templates/             # HTML templates
├── tests/                 # Test suite
│   ├── test_ai_models.py  # AI service tests
│   └── test_storage.py    # Storage service tests
├── utils/                 # Utility functions
├── app.py                 # Application factory
├── config.py             # Configuration
├── requirements.txt      # Python dependencies
└── wsgi.py              # WSGI entry point
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd learning-platform
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:8080`

## API Endpoints

### Storage Service

#### Upload File
```http
POST /storage/upload
Content-Type: multipart/form-data

file: <file>
```

#### Download File
```http
GET /storage/download/<filename>
```

### AI Service

#### Generate CV
```http
POST /ai/generate-cv
Content-Type: application/json

{
  "name": "John Doe",
  "skills": ["Python", "Cloud Computing"]
}
```

#### Get Job Recommendations
```http
POST /ai/recommend-jobs
Content-Type: application/json

{
  "skills": ["Cloud Computing", "DevOps"]
}
```

## Testing

Run the test suite:
```bash
python -m pytest
```

## Development

### Adding New Features

1. Create new routes in the appropriate blueprint
2. Add corresponding templates if needed
3. Update tests to cover new functionality
4. Document API changes in this README

### Code Style

- Follow PEP 8 guidelines
- Use type hints for better code documentation
- Write docstrings for functions and classes
- Keep functions small and focused

## Deployment

The application is configured for deployment on various platforms:

- Vercel: Uses `vercel.json` configuration
- Docker: Uses `Dockerfile` for containerization
- Traditional hosting: Uses `gunicorn` with `wsgi.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
