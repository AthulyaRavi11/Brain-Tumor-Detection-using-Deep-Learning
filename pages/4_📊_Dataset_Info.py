import streamlit as st

st.title("📊 Dataset Information")

st.markdown("""
### Dataset Overview
- Brain MRI images
- Public academic dataset (Kaggle)
- Fully anonymized

### Classes
- Tumor
- No Tumor

### Challenges
- Class imbalance
- MRI contrast variations
""")

st.info("Dataset used strictly for research & academic purposes.")
