from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)
UploadFolder = 'uploads'
os.makedirs(UploadFolder, exist_ok=True)

@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No Image Provided'}, 400

    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    output = remove(img)
    output_io = io.BytesIO()
    output.save(output_io, format="PNG")
    output_io.seek(0)

    return send_file(output_io, mimetype='image/png')

@app.route("/")
def index():
    return 'Removal API using REMBG is running!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)