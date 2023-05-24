import json

import requests
import streamlit as st

st.title("YOLO Coder QnA 🔎")

if 'is_post' not in st.session_state:
    st.session_state['is_post'] = True

# Form


base_url = st.text_input("Base URL", "https://aiehackathon2023.replit.app")
option = st.selectbox(
        "Endpoints",
        ("analysis", "supplier", "product", "order"),
    )
http_method = st.radio(
        "HTTP method 👉",
        key="disabled",
        options=["GET", "POST"]
    )

if http_method == 'POST':
    payload = st.text_area('JSON Payload', "", height=None)

# query = form.text_input(f"{base_url} {option}")
form = st.form("api_form")

submit = form.form_submit_button("Submit")

if submit:
    headers = {'Content-Type': 'application/json'}

    url = f"{base_url}/{option}"

    print(option)
    if http_method == 'GET':
        payload = ""
        response = requests.get(url, headers=headers)
        # print(response.json())

    if http_method == 'POST':

        payload = " ".join(payload.split())
        json_file = json.dumps(payload)
        print(json_file)
        response = requests.post(url, data=json_file, headers=headers)

    st.json(response.json(), expanded=True)

