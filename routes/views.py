from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.course import CourseRepository
from models.quiz import QuizRepository
from models.job import JobRepository
from services.ai_service import AIService

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    return render_template('index.html')

@views_bp.route('/courses')
def courses():
    courses = CourseRepository.get_all()
    return render_template('courses.html', courses=courses)

@views_bp.route('/course/<int:course_id>')
def course_detail(course_id):
    course = CourseRepository.get_by_id(course_id)
    quiz = QuizRepository.get_by_course_id(course_id)
    return render_template('course_detail.html', course=course, quiz=quiz)

@views_bp.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    quiz = QuizRepository.get_by_id(quiz_id)
    if request.method == 'POST':
        score = 0
        total = len(quiz.questions)
        for question in quiz.questions:
            answer = request.form.get(f'question_{question["id"]}')
            if answer and int(answer) == question['correct_answer']:
                score += 1
        return render_template('quiz_results.html', score=score, total=total)
    return render_template('quiz.html', quiz=quiz)

@views_bp.route('/jobs')
def jobs():
    jobs = JobRepository.get_all()
    return render_template('jobs.html', jobs=jobs)

@views_bp.route('/cv-builder', methods=['GET', 'POST'])
def cv_builder():
    if request.method == 'POST':
        name = request.form.get('name')
        skills = request.form.getlist('skills')
        cv_content = AIService.generate_cv_content(name, skills)
        return render_template('cv_preview.html', cv=cv_content)
    return render_template('cv_builder.html')