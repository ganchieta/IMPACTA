import streamlit as st
import uuid
import os

st.title('😉 Automai')

uploaded_file = st.file_uploader("Selecione o seu arquivo", accept_multiple_files=False, type=['mp4'])

if uploaded_file is not None:
    mp4_filename = uploaded_file.name
    mp3_filename = uuid.uuid4().hex + ".mp3"

    # Salvar o arquivo MP4 temporariamente
    temp_mp4_path = os.path.join("temp", mp4_filename)
    os.makedirs("temp", exist_ok=True)  #