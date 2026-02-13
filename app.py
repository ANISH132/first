import streamlit as st
import os

st.set_page_config(page_title="Valentine Host", layout="centered")


html_path = "index.html"
if not os.path.exists(html_path):
    st.error("index.html not found in the same folder as app.py. Please place index.html here.")
else:
    with open(html_path, "r", encoding="utf-8") as f:
        html_template = f.read()
    html = html_template.replace("{{IMAGE_DATA}}", "")
    st.components.v1.html(html, height=820, scrolling=True)
