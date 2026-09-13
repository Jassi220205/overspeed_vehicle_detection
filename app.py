from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from vehicle import process_video

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'video' not in request.files:
            return redirect(request.url)
            
        file = request.files['video']
        if file.filename == '':
            return redirect(request.url)

        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], "output.mp4")

        file.save(input_path)

        # Run detection pipeline and collect logs
        _, logs = process_video(input_path, output_path)

        return render_template('index.html', video_url='/outputs/output.mp4', logs=logs)

    return render_template('index.html')

# Serve output videos using send_from_directory for reliable browser streaming
@app.route('/outputs/<path:filename>')
def serve_output_video(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)