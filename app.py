import streamlit as st 
import tensorflow as tf 
import numpy as np 
from PIL import Image

st.title('TumorLensB0 | Brain Tumor Detection AI')

model = tf.keras.models.load_model('brain_tumor_model.h5')
class_names = ['Glioma', 'Meningioma', 'No tumor', 'Pituitary']

uploaded_file = st.file_uploader("Upload an MRI image:", type=['png', 'jpg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded MRI Image', width=300)
    
    resized_image = image.resize((224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(resized_image)
    image_array = np.expand_dims(image_array, axis=0)
    
    predictions = model.predict(image_array)
    highest_prediction_index = np.argmax(predictions)
    confidence = predictions.max() * 100
    
    if confidence < 80.0:
        st.warning('The image does not resemble a brain MRI or CT scan.')
    else:
        st.success(f'**Result:** {class_names[highest_prediction_index]}')
        st.write(f'**Confidence:** {confidence:.2f}%')
    
    
