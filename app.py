from flask import Flask, render_template, request, send_file
import requests
import os
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

REMOVE_BG_API_KEY = "9XTqrBU4iuSB32yTsFQb1LFw"  # Tumhari remove.bg API key


def remove_background(image_path):
    with open(image_path, 'rb') as img_file:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': img_file},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVE_BG_API_KEY}
        )
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Background removal failed:", response.text)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    data_url = request.form["imageData"]
    header, encoded = data_url.split(",", 1)
    image_data = base64.b64decode(encoded)

    image_path = os.path.join(UPLOAD_FOLDER, "captured.png")
    with open(image_path, "wb") as f:
        f.write(image_data)

    no_bg = remove_background(image_path)

    final_path = os.path.join(UPLOAD_FOLDER, "final_photo.pdf")
    no_bg.save(final_path, "PDF")

    return send_file(final_path, mimetype="application/pdf")


if __name__ == "__main__":
    app.run(debug=True)
