from flask import Flask, render_template, request, redirect
from pathlib import Path
import os
from deepface import DeepFace
from werkzeug.utils import secure_filename
from pprint import pprint
import base64

app = Flask(__name__)

app.config['IMAGE_UPLOADS'] =  str(Path(__file__).parent / 'uploads')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare-images', methods=['GET', 'POST'])
def compare_images():
    if request.files:
        id_photo = request.files['id-photo']
        photo = request.files['photo']
        print(id_photo)
        print(photo)
        id_photo_extension = os.path.splitext(id_photo.filename)[1][1:]
        photo_extension = os.path.splitext(photo.filename)[1][1:]
        print(id_photo_extension)
        print(photo_extension)
        id_photo_data = base64.b64encode(id_photo.read()).decode()
        id_photo_data = 'data:image/' + id_photo_extension + ';base64,' + id_photo_data
        photo_data = base64.b64encode(photo.read()).decode()
        photo_data = 'data:image/' + photo_extension + ';base64,' + photo_data
        print('DeepFace verify starting...')
        result = DeepFace.verify(id_photo_data, photo_data)
        pprint(result)
        return render_template('compare-images.html', is_same_face=result['verified'])
    
    return render_template('compare-images.html')

if __name__ == '__main__':
    app.run(debug=True)
