import os
import cv2
import numpy as np

from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = load_model("model/image_classifier.h5")


classes = ['cat', 'dog']


def predict_image(image_path):
    image = cv2.imread(image_path)

    image = cv2.resize(image, (128, 128))
    image = image.astype("float32") / 255.0

    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)

    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return classes[class_index], confidence


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    label, confidence = predict_image(filepath)

    return render_template(
        "result.html",
        image_path=filepath,
        prediction=label,
        confidence=round(confidence * 100, 2)
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)