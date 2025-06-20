# Proyecto de Detecció de Emociones

## Prerequisitos:

- Windows 11

- Python 3.11.9

- TensorFlow

## Instalación de librerías

Ejecutar las siguientes sentencias:

```bash
pip install flask tensorflow numpy pillow
```

## Ejecución

Ejecutar el modelo:

```bash
## Ejecutarlo en la raiz
python train_model.py
```

Ejecuar el servicio web para probar el modelo:

```bash
## Ejecutarlo en la carpeta 'app'
python app.py
```

## Pruebas

Para probar, se puede usar la herramienta `Postman` con el siguiente:

```json
{
    "tipo":"POST",
    "url":"http://127.0.0.1:5000/predict",
    "parametros": {
        "tipo":"form-data2",
        "param": {
            "key":"image",
            "tipo":"file",
            "value":"un archivo de una imagen de un perro"
        }
    }
} 
```