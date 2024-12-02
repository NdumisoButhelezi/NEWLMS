from flask import Flask, send_from_directory, render_template
import os
from routes.storage import storage_bp
from routes.ai_models import ai_bp
from routes.views import views_bp
from config import Config

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')
            
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY', 'dev')

# Register blueprints
app.register_blueprint(storage_bp, url_prefix='/storage')
app.register_blueprint(ai_bp, url_prefix='/ai')
app.register_blueprint(views_bp)

# Error handlers
@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', error=500), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', error=404), 404

# Required for Vercel
app.debug = False

if __name__ == '__main__':
    app.run()