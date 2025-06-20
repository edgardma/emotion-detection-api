from tensorflow.keras.models import load_model
import os

# Ruta al modelo original en .h5
INPUT_MODEL_PATH = "emotion_model.h5"

# Carpeta donde se guardará el modelo exportado en formato SavedModel
OUTPUT_MODEL_DIR = "emotion_model_tf"

# Cargar modelo
print(f"🔄 Cargando modelo desde {INPUT_MODEL_PATH}...")
model = load_model(INPUT_MODEL_PATH, compile=False)

# Exportar en formato SavedModel
print(f"💾 Exportando modelo a {OUTPUT_MODEL_DIR}/ en formato SavedModel...")
model.export(OUTPUT_MODEL_DIR)

print("✅ Modelo exportado exitosamente.")
