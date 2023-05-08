from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare-images', methods=['POST'])
def compare_images():
    return 'Compare Images'

if __name__ == '__main__':
    app.run(debug=True)
