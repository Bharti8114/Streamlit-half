from tkinter import Image

import streamlit as st
import pandas as pd
from PIL import Image

st.subheader("Loading the CSV files")
uploaded_file = st.file_uploader("Upload the CSV file : ", type=['csv', 'xls'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.table(df.head())

st.subheader("Dealing with image")
st.image('C:/Users/Deepak/OneDrive/Pictures/147581.jpg')

uploaded_image = st.file_uploader("Upload the image : ", type = ['png','jpg'])
if uploaded_image is not None:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image")

st.subheader("Working with Videos")
video_flie = st.file_uploader("Upload the video file : ", type = ['mkv','mp4'])
if video_flie is not None:
    st.video(video_flie , start_time= 0)


st.subheader("Working with Audio")
audio_file = st.file_uploader("Upload the Audio file : ", type = ['wav','mp3'])
if video_flie is not None:
    st.audio(audio_file.read())


