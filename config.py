import os
from pathlib import Path
from typing import Dict, Any

class Config:
    """Application configuration."""
    # Base directory of the project
    BASE_DIR: Path = Path(__file__).resolve().parent
    
    # Storage configuration
    UPLOAD_FOLDER: Path = BASE_DIR / 'storage'
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 16MB max file size
    
    # Flask configuration
    DEBUG: bool = True
    TESTING: bool = False
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """Get configuration dictionary."""
        return {
            key: value for key, value in cls.__dict__.items()
            if not key.startswith('__') and not callable(value)
        }
    
    @classmethod
    def init_app(cls) -> None:
        """Initialize application configuration."""
        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)