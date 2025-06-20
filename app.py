
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)
model = load_model('model/emotion_model.h5')  # Cargar el modelo entrenado

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener el archivo de imagen cargado
    img_file = request.files['image']
    
    # Convertir el archivo cargado a una imagen con PIL (Pillow)
    img = Image.open(img_file.stream)
    
    # Redimensionar la imagen a (224, 224) como espera el modelo
    img = img.resize((224, 224))

    # Convertir la imagen en un array que pueda ser usado por TensorFlow
    img_array = np.array(img)

    # Asegurarse de que la imagen tenga 3 canales (RGB)
    if img_array.shape[-1] != 3:
        img_array = np.repeat(img_array[..., np.newaxis], 3, -1)

    # Normalizar la imagen
    img_array = img_array / 255.0

    # Expander dimensiones para hacer batch (el modelo espera un lote de imágenes)
    img_array = np.expand_dims(img_array, axis=0)

    # Hacer la predicción
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    # Mapear el índice a una clase
    emotion = ['happy', 'sad', 'angry'][predicted_class[0]]
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
