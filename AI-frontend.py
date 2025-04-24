
from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model("keras_model.h5")  # Your trained model

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    img = Image.open(file).resize((224, 224))  # Adjust based on model input
    img_array = np.array(img) / 255.0
    prediction = model.predict(np.expand_dims(img_array, axis=0))
    return jsonify({"class": str(np.argmax(prediction)), "confidence": float(np.max(prediction))})

if __name__ == "__main__":
    app.run()
