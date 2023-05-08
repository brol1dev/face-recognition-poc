from flask import Flask, render_template, request, redirect
from pathlib import Path
import os
from deepface import DeepFace
from werkzeug.utils import secure_filename
from pprint import pprint

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
        id_photo_filename = secure_filename(id_photo.filename)
        photo_filename = secure_filename(photo.filename)
        print(id_photo_filename)
        print(photo_filename)
        id_photo_path = os.path.join(app.config['IMAGE_UPLOADS'], id_photo_filename)
        photo_path = os.path.join(app.config['IMAGE_UPLOADS'], photo_filename)
        print(id_photo_path)
        print(photo_path)
        id_photo.save(id_photo_path)
        photo.save(photo_path)
        print('saved images')
        # print('DeepFace verify starting...')
        # result = DeepFace.verify(id_photo_path, photo_path)
        # pprint(result)
        # return render_template('compare-images.html', is_same_face=result['verified'])
    
    return render_template('compare-images.html')

if __name__ == '__main__':
    app.run(debug=True)
