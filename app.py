import streamlit as st
from PIL import Image
from numpy import asarray
from deepface import DeepFace

st.title('Is it the same face?')

def main():
    column1, column2 = st.columns(2)  
    with column1:
        image1 = st.file_uploader("Select Photo ID", type=["jpg","png"])
        
    with column2:
        image2 = st.file_uploader("Select Selfie", type=["jpg","png"])
    if (image1 is not None) & (image2  is not None):
        col1, col2 = st.columns(2)
        image1 =  Image.open(image1)
        image2 =  Image.open(image2)
        with col1:
            st.image(image1)
        with col2:
            st.image(image2)

        data1 = asarray(image1)
        data2 = asarray(image2)
        result = DeepFace.verify(data1, data2)
        if (result['verified']):
            st.success('✅ It is the same person 😀 👍')
        else:
            st.error('❌ It is not the same person 🙁')

main()
