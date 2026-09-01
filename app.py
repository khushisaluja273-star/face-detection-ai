import os
import cv2
import uuid
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
RESULT_FOLDER = os.path.join('static', 'results')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# OpenCV ka pre-trained Haar Cascade classifier face detection ke liye
CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)


def detect_faces(image_path, output_path):
    """Image me faces detect karke bounding box draw karta hai."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,   # image ko kitna chhota karke scan kare
        minNeighbors=5,    # false positives kam karne ke liye
        minSize=(30, 30)   # sabse chhota face size jo detect hoga
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(output_path, img)
    return len(faces)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            ext = os.path.splitext(file.filename)[1]
            unique_name = f"{uuid.uuid4().hex}{ext}"

            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            result_path = os.path.join(app.config['RESULT_FOLDER'], unique_name)

            file.save(upload_path)
            face_count = detect_faces(upload_path, result_path)

            return render_template(
                'index.html',
                result_image=url_for('static', filename=f'results/{unique_name}'),
                face_count=face_count
            )

    return render_template('index.html', result_image=None, face_count=None)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
