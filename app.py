import streamlit as st

st.set_page_config(
    page_title="Brain Tumor Detection System",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Brain Tumor Detection System")

st.markdown("""
### AI-assisted MRI Analysis using Deep Learning

This project presents a **deep learning–based system** for detecting the
presence of brain tumors from **MRI scans**.

The system is designed for **academic and research purposes**, and demonstrates
how convolutional neural networks can assist in medical image analysis.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 What does this system do?")
    st.markdown("""
    - Accepts MRI brain images  
    - Preprocesses and normalizes scans  
    - Uses a trained CNN model  
    - Predicts **Tumor / No Tumor**  
    - Displays confidence score  
    """)

with col2:
    st.subheader("🧠 Technologies Used")
    st.markdown("""
    - Python  
    - TensorFlow / Keras  
    - Convolutional Neural Networks  
    - Transfer Learning (MobileNetV2)  
    - Streamlit (UI)
    """)

st.markdown("---")

st.subheader("📂 Project Sections")

st.markdown("""
Use the **sidebar navigation** to explore:

- **Prediction** – Upload MRI images and get results  
- **Model Info** – Architecture and training details  
- **Dataset Info** – Dataset description  
- **Results** – Evaluation and performance  
- **Future Scope** – Planned enhancements  
- **About** – Project overview  
""")

st.info("⚠️ This system is for educational and research use only.")
