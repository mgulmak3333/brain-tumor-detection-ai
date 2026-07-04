# Brain Tumor Detection AI 🧠🔬

<p align="left">
  <img src="https://medicine.washu.edu/app/uploads/2021/02/GlioblastomaBranScans-700x467.jpg" alt="Brain MRI Scans" width="500">
</p>

<p align="left">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="TensorFlow">
  <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

---

## 🚀 Live Demo & Model Links
* **Web Application:** Built with Streamlit.
* **Trained Model & Dataset:** You can access the trained model (`brain_tumor_model.h5`) and the source dataset on Kaggle via [Brain Tumor MRI Data by Tom Backert](https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data).

---

## 📊 Dataset & Classes
The model is trained to classify MRI scans into four distinct categories:
1. **Glioma**
2. **Meningioma**
3. **No Tumor**
4. **Pituitary**

---

## 🛠️ Tech Stack & Dependencies
* **Deep Learning Framework:** TensorFlow / Keras
* **Model Architecture:** EfficientNet-B0 (Transfer Learning)
* **Web Interface:** Streamlit
* **Data Processing:** NumPy, Pillow (PIL)

---

## 💻 Installation & Local Setup

Follow these steps to run the Streamlit application on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/mgulmak3333/brain-tumor-detection-ai
cd brain-tumor-detection-ai

```

### 2. Install Requirements

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt

```

### 3. Download the Model

Download the `brain_tumor_model.h5` file from the Kaggle link provided above and place it into the root directory of this project.

### 4. Run the Streamlit App

```bash
streamlit run app.py

```

---

## 🎯 Citation

If you use the dataset or want to reference the source materials in your work, please credit the original author:

```text
Brain Tumor MRI Data by Tom Backert
URL: [https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data](https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data)

```

```
