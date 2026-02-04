import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Prediction", layout="wide")

st.title("🔍 MRI Tumor Prediction")

st.markdown("""
Upload a brain MRI scan to detect whether a tumor is present.
""")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("brain_tumor_model.h5")

model = load_model()

confidence_threshold = st.slider(
    "Detection Sensitivity",
    0.4, 0.9, 0.5, 0.05
)

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    col1, col2 = st.columns([1, 1.2])

    image = Image.open(uploaded_file).convert("RGB")

    with col1:
        st.image(image, caption="Uploaded MRI", use_column_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)
    tumor_prob = float(prediction[0][0])

    with col2:
        st.subheader("Prediction Result")

        if abs(tumor_prob - 0.5) < 0.1:
            st.warning("Model confidence is low. Result may be uncertain.")

        if tumor_prob > confidence_threshold:
            st.error("🟥 Tumor Detected")
            st.write(f"Confidence: {tumor_prob*100:.2f}%")
            st.progress(tumor_prob)
        else:
            st.success("🟩 No Tumor Detected")
            st.write(f"Confidence: {(1-tumor_prob)*100:.2f}%")
            st.progress(1 - tumor_prob)

        st.subheader("Probability Distribution")
        st.bar_chart({
            "Tumor": tumor_prob * 100,
            "No Tumor": (1 - tumor_prob) * 100
        })

st.warning("⚠️ Not for clinical diagnosis.")
