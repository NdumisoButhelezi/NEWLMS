from flask import Blueprint, request
from services.ai_service import AIService
from utils.response import success_response, error_response
from utils.validators import validate_skills

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/generate-cv', methods=['POST'])
def generate_cv():
    data = request.get_json()
    
    if not data or 'name' not in data or 'skills' not in data:
        return error_response('Missing required fields')
    
    if not validate_skills(data['skills']):
        return error_response('Invalid skills format')
    
    cv_content = AIService.generate_cv_content(data['name'], data['skills'])
    return success_response(data=cv_content)

@ai_bp.route('/recommend-jobs', methods=['POST'])
def recommend_jobs():
    data = request.get_json()
    
    if not data or 'skills' not in data:
        return error_response('Skills are required')
    
    if not validate_skills(data['skills']):
        return error_response('Invalid skills format')
    
    recommendations = AIService.get_job_recommendations(data['skills'])
    return success_response(data={'recommendations': recommendations})