from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

# Import route blueprints
from routes.auth_routes import auth_bp
from routes.meme_routes import meme_bp
from routes.admin_routes import admin_bp

app = Flask(__name__, static_folder='public')
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = os.path.join('public', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file size

# Root route - Serve static HTML
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('public', path)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(meme_bp, url_prefix='/memes')
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    print('AWS Meme Museum running on port 3000')
    app.run(host='0.0.0.0', port=3000, debug=True)
