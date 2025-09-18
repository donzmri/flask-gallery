from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Folder untuk file gambar
IMAGE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

@app.route('/')
def home():
    return "Flask Gallery API is running. Access your files via /images/<filename>"

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
