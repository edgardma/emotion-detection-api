from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)
model = load_model('model/emotion_model.h5')  # Cargar el modelo entrenado

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    try:
        img_file = request.files['image']
        img = Image.open(img_file.stream)
        img = img.resize((224, 224))
        img_array = np.array(img)

        if img_array.shape[-1] != 3:
            img_array = np.repeat(img_array[..., np.newaxis], 3, -1)

        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_class = int(np.argmax(predictions))

        return jsonify({'predicted_class': predicted_class})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
