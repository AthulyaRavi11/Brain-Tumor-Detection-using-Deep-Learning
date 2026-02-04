import streamlit as st

st.title("🧠 Model Information")

st.markdown("""
### Model Architecture
- Convolutional Neural Network (CNN)
- Transfer Learning using **MobileNetV2**
- Sigmoid output layer for binary classification

### Training Details
- Loss Function: Binary Cross Entropy
- Optimizer: Adam
- Image Size: 224 × 224

### Why CNN?
CNNs efficiently learn spatial features from MRI images such as
edges, textures, and abnormal patterns.
""")
