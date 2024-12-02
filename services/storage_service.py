import os
from typing import Set, Tuple, Union
from werkzeug.utils import secure_filename
from flask import current_app
from werkzeug.datastructures import FileStorage

class StorageService:
    ALLOWED_EXTENSIONS: Set[str] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}

    @classmethod
    def save_file(cls, file: FileStorage) -> Tuple[bool, Union[str, None], Union[str, None]]:
        """Save file to storage and return status, filename, and error message."""
        if not file or file.filename == '':
            return False, None, "No file selected"

        if not cls._is_allowed_file(file.filename):
            return False, None, "File type not allowed"

        filename = secure_filename(file.filename)
        try:
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return True, filename, None
        except Exception as e:
            return False, None, f"Error saving file: {str(e)}"

    @staticmethod
    def _is_allowed_file(filename: str) -> bool:
        """Check if the file extension is allowed."""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in StorageService.ALLOWED_EXTENSIONS