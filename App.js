
import React, { useState } from 'react';
import { View, Text, Button, Image } from 'react-native';
import ImagePicker from 'react-native-image-picker';
import axios from 'axios';

const App = () => {
  const [imageUri, setImageUri] = useState(null);
  const [emotion, setEmotion] = useState('');

  const pickImage = () => {
    ImagePicker.showImagePicker({}, response => {
      if (response.uri) {
        setImageUri(response.uri);
        uploadImage(response.uri);
      }
    });
  };

  const uploadImage = async (uri) => {
    const formData = new FormData();
    formData.append('image', {
      uri,
      type: 'image/jpeg',
      name: 'image.jpg',
    });

    try {
      const result = await axios.post('http://<tu-ip>:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setEmotion(result.data.emotion);
    } catch (error) {
      console.error('Error al obtener la predicción', error);
    }
  };

  return (
    <View>
      <Button title="Seleccionar Imagen" onPress={pickImage} />
      {imageUri && <Image source={{ uri: imageUri }} style={{ width: 300, height: 300 }} />}
      {emotion && <Text>El animal está {emotion}</Text>}
    </View>
  );
};

export default App;
