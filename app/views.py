from flask import Blueprint, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from model.detect import detect_faces

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No file part'

    file = request.files['video']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('videos', filename)
        file.save(file_path)

        # Create 'outputs' directory if it doesn't exist
        output_dir = 'outputs'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Process the video
        output_video_path = detect_faces(file_path)
        return f"Video saved to{output_video_path}",send_from_directory(directory=os.path.dirname(output_video_path), path=os.path.basename(output_video_path))
    return 'Video processed'