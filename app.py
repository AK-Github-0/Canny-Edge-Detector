import streamlit as st
from PIL import Image
import os
import cv2 as cv
import matplotlib.pyplot as plt

st.title("App for canny")
upimage = st.button('Upload Image')
apply = st.button('Apply canny')
lowthreshhold = st.slider("Select the low threshhold", 0, 100)
highthreshhold = st.slider("Select the high threshhold", 100, 300)


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


if __name__ == '__main__':
    if st.checkbox('Select a file in current directory'):
        folder_path = '.'
        if st.checkbox('Change directory'):
            folder_path = st.text_input('Enter folder path', '.')
        filename = file_selector(folder_path=folder_path)
        st.write('You selected `%s`' % filename)

    if upimage:
        img = Image.open(filename)
        a = st.image(img, width=200)

    if apply:
        images = cv.imread(filename)
        edges = cv.Canny(images,lowthreshhold,highthreshhold)
        st.image(edges,width=200)

    about = st.button("About")
    if about:
        st.write("I am Abdullah Khan, Registration number 2020024. :smile: ")