# Learning Platform with Simulated Cloud Services

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
