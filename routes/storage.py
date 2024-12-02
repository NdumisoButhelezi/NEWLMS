from flask import Blueprint, request, send_from_directory, current_app
from services.storage_service import StorageService
from utils.response import success_response, error_response

storage_bp = Blueprint('storage', __name__)

@storage_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return error_response('No file part')
        
    file = request.files['file']
    success, filename, error = StorageService.save_file(file)
    
    if not success:
        return error_response(error)
    
    return success_response(
        data={'filename': filename},
        message='File uploaded successfully'
    )

@storage_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory(
            current_app.config['UPLOAD_FOLDER'],
            filename,
            as_attachment=True
        )
    except FileNotFoundError:
        return error_response('File not found', 404)