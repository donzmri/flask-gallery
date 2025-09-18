from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Folder tempat menyimpan gambar di dalam "static/images"
IMAGE_FOLDER = os.path.join(os.getcwd(), "static", "images")

@app.route("/")
def home():
    return "Flask Gallery API is running. Access images via /images/<filename>"

# Route untuk mengakses gambar
@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == "__main__":
    app.run()
