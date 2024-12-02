from typing import Set

def validate_file_extension(filename: str, allowed_extensions: Set[str]) -> bool:
    """Validate if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def validate_skills(skills: list) -> bool:
    """Validate if skills list is properly formatted."""
    return isinstance(skills, list) and all(isinstance(skill, str) for skill in skills)