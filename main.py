import json

import requests
import streamlit as st

st.title("YOLO Coder QnA 🔎")


# Form
form = st.form("api_form")

base_url = form.text_input("Base URL", "https://aiehackathon2023.replit.app")
option = form.selectbox(
        "Endpoints",
        ("analysis", "supplier", "product", "order"),
    )
http_method = form.radio(
        "HTTP method 👉",
        key="disabled",
        options=["GET", "POST"]
    )

payload = form.text_area('JSON Payload', '''
    
    ''')


# query = form.text_input(f"{base_url} {option}")


submit = form.form_submit_button("Submit")

if submit:
    headers = {'Content-Type': 'application/json'}

    url = f"{base_url}/{option}"

    print(option)
    payload = ""
    if http_method == 'GET':
        payload = ""
        response = requests.get(url, headers=headers)
        # print(response.json())

    if http_method == 'POST':
        response = requests.post(url, data=json.dumps(payload), headers=headers)

    st.json(response.json(), expanded=True)
    # text = st.text_area("HTTP Response", str(response.json()))


# form = st.form("my_form")
# input_form = form.text_area("Enter your questions")
# form.form_submit_button("Submit")



# start_phrase = 'Write a tagline for an ice cream shop. '
# response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
# text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()

# # print the response
# print(response['choices'][0]['message']['content'])
