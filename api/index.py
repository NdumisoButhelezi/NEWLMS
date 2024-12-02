from flask import Flask, send_from_directory
import os
from routes.storage import storage_bp
from routes.ai_models import ai_bp
from routes.views import views_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY', 'dev')

# Initialize configuration
Config.init_app()

# Register blueprints
app.register_blueprint(storage_bp, url_prefix='/storage')
app.register_blueprint(ai_bp, url_prefix='/ai')
app.register_blueprint(views_bp)

# Serve static files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Required for Vercel
app.debug = False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)