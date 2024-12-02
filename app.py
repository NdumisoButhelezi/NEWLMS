from flask import Flask
from routes.storage import storage_bp
from routes.ai_models import ai_bp
from routes.views import views_bp
from config import Config

def create_app(config_class=Config):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'dev'  # Change this to a secure key in production
    
    # Initialize configuration
    config_class.init_app()
    
    # Register blueprints
    app.register_blueprint(storage_bp, url_prefix='/storage')
    app.register_blueprint(ai_bp, url_prefix='/ai')
    app.register_blueprint(views_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)