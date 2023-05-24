# OPENAI
import openai
import requests
import streamlit as st
from streamlit_chat import message

openai.api_type = "azure"
openai.api_base = "https://testofgptapiinitial.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "8412267798784cdfa103c445c69f603d"

# init msg to chat
basic =[
    {
        "role": "system",
        "content": "You are an AI assistant that helps users format their API requests. Endpoints are Analysis, Supplier, Order and Product. Users will ask you about ways to enter information via API and you have to provide them with request bodies that would make for successful calls, based on the examples you have. If users don't provide all the information needed in the request fields, your response should be a request for such information instead a sample payload. You should NEVER output a json response unless the user has provided the value for all the fields"
    },
    {
        "role": "user",
        "content": "Successful POST request to the Analysis endpoint"
    },
    {
        "role": "assistant",
        "content": "{ \n \"name\": \"Sample Analysis\", \n \"country\": \"United States\", \n \"start_date\": \"2022-01-01\", \n \"end_date\": \"2022-01-31\", \n \"products\": [ \n { \n \"brand_name\": \"BRAND A\", \n \"target_audience_name\": \"AUDIENCE A\", \n \"reach\": 1000.0, \n \"cost\": 1000.0 \n },\n { \n \"brand_name\": \"BRAND B\", \n \"target_audience_name\": \"AUDIENCE B\", \n \"reach\": 1000.0, \n \"cost\": 1000.0 \n },\n { \n \"brand_name\": \"BRAND C\", \n \"target_audience_name\": \"AUDIENCE C\", \n \"reach\": 1000.0, \n \"cost\": 1000.0 \n }\n ], \n \"audiences\": { \n \"Audience A\": { \n \"gender_flag\": \"True\", \n \"start_age_qty\": 18, \n \"end_age_qty\": 34 \n }, \n \"Audience B\": { \n \"gender_flag\": \"False\", \n \"start_age_qty\": 25, \n \"end_age_qty\": 50 \n } \n } \n} "
    },
    {
        "role": "user",
        "content": "Successful POST request to the Supplier endpoint"
    },
    {
        "role": "assistant",
        "content": "{ \n \"name\": \"Sample Supplier\", \n \"raw_materials\": [ \n { \n \"raw_material\": { \n \"name\": \"Raw Material A\", \n \"description\": \"This is a description for Raw Material A\", \n \"type\": \"Type A\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"price\": 10.0, \n \"min_order_quantity\": 5 \n },\n { \n \"raw_material\": { \n \"name\": \"Raw Material B\", \n \"description\": \"This is a description for Raw Material B\", \n \"type\": \"Type B\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"price\": 20.0, \n \"min_order_quantity\": 50 \n },\n ], \n \"contact_person\": \"John Doe\", \n \"contact_number\": \"1234567890\" \n} "
    },
    {
        "role": "user",
        "content": "Successful POST request to the Order endpoint"
    },
    {
        "role": "assistant",
        "content": "{ \n \"customer\": { \n \"name\": \"John Doe\", \n \"email\": \"johndoe@example.com\", \n \"phone\": \"1234567890\", \n \"address\": \"123 Main St\", \n \"city\": \"Anytown\", \n \"lat\": 40.7128, \n \"lon\": -74.0060 \n }, \n \"lines\": [ \n { \n \"product\": { \n \"name\": \"Product A\", \n \"category\": \"femcare\", \n \"unit_price\": 10.0 \n }, \n \"quantity\": 5 \n }, \n { \n \"product\": { \n \"name\": \"Product B\", \n \"category\": \"grooming\", \n \"unit_price\": 20.0 \n }, \n \"quantity\": 10 \n } \n ] \n}"
    },
    {
        "role": "user",
        "content": "Successful POST request to the Product endpoint"
    },
    {
        "role": "assistant",
        "content": "{ \n \"name\": \"Sample Product\", \n \"raw_materials\": [ \n { \n \"raw_material\": { \n \"name\": \"Product A\", \n \"description\": \"Sample description A\", \n \"type\": \"Type A\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"quantity\": 10 \n },\n {\n \"raw_material\": { \n \"name\": \"Product B\", \n \"description\": \"Sample description B\", \n \"type\": \"Type b\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"quantity\": 30 \n }\n ] \n} "
    },
    {
        "role": "user",
        "content": "I want to enter a new supplier"
    },
    {
        "role": "assistant",
        "content": "I will need some additional information: Supplier name, raw materials (name, description, type and unit of measurement for each material as well as its price and minimum order quantity. Additionally I will need a contact person and a contact number"
    }
]

# Start of page
st.set_page_config(
    page_title="Yolo Coder Chat",
    page_icon=":robot:"
)


st.header("YOLO Coder Helper - Demo v1.0")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(msg):
     basic.append(
          {"role":"user",
           "content": msg}
         )
     response = openai.ChatCompletion.create(
          engine="ChatGPT0301",
          messages=basic,
          temperature=0.5,
          max_tokens=800,
          top_p=0.95,
          frequency_penalty=0,
          presence_penalty=0,
          stop=None)
     
     print(response["choices"][0]["message"]["content"])
     return response["choices"][0]["message"]["content"]

def get_text():
    input_text = st.text_input("You: ","Hello", key="input")
    return input_text 

user_input = get_text()

if user_input:
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
