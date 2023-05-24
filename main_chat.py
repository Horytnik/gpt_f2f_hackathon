# OPENAI
import openai
import requests
import streamlit as st
from streamlit_chat import message
#from api import post_request
import json


openai.api_type = "azure"
openai.api_base = "https://testofgptapiinitial.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "8412267798784cdfa103c445c69f603d"

def post_request(data: json, api: str) -> bool:

    url = f"https://aiehackathon2023.replit.app/{api}"

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.status_code)

    print(response.text)
    return response.status_code

# init msg to chat
basic = [
    {
        "role": "system",
        "content": "You are an AI assistant that outputs either JSON POST request bodies or requests for the missing information to format those. The requests can be for Analysis, Supplier, Order and Product. Given the category that the user asks about (one of Analysis, Supplier, Order and Product), ask for all the needed fields to format a JSON request body. Once you have all of them, output the JSON request. If you do not have all of the JSON fields, ask the user for them. If you would output anything similar to JSON, output the JSON code instead"
    },
    {
        "role": "user",
        "content": "Successful JSON body for a POST request to the endpoint Analysis"
    },
    {
        "role": "assistant",
        "content": "{ \n \"name\": \"Sample Analysis\", \n \"country\": \"United States\", \n \"start_date\": \"2022-01-01\", \n \"end_date\": \"2022-01-31\", \n \"products\": [ \n { \n \"brand_name\": \"BRAND A\", \n \"target_audience_name\": \"AUDIENCE A\", \n \"reach\": 1000.0, \n \"cost\": 1000.0 \n },\n { \n \"brand_name\": \"BRAND B\", \n \"target_audience_name\": \"AUDIENCE B\", \n \"reach\": 1000.0, \n \"cost\": 1000.0 \n },\n { \n \"brand_name\": \"BRAND C\", \n \"target_audience_name\": \"AUDIENCE C\", \n \"reach\": 1000.0, \n \"cost\": 1000.0 \n }\n ], \n \"audiences\": { \n \"Audience A\": { \n \"gender_flag\": \"True\", \n \"start_age_qty\": 18, \n \"end_age_qty\": 34 \n }, \n \"Audience B\": { \n \"gender_flag\": \"False\", \n \"start_age_qty\": 25, \n \"end_age_qty\": 50 \n } \n } \n} "
    },
    {
        "role": "user",
        "content": "Successful JSON body for a POST request to the endpoint Supplier"
    },
    {
        "role": "assistant",
        "content": "{ \n \"name\": \"Sample Supplier\", \n \"raw_materials\": [ \n { \n \"raw_material\": { \n \"name\": \"Raw Material A\", \n \"description\": \"This is a description for Raw Material A\", \n \"type\": \"Type A\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"price\": 10.0, \n \"min_order_quantity\": 5 \n },\n { \n \"raw_material\": { \n \"name\": \"Raw Material B\", \n \"description\": \"This is a description for Raw Material B\", \n \"type\": \"Type B\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"price\": 20.0, \n \"min_order_quantity\": 50 \n },\n ], \n \"contact_person\": \"John Doe\", \n \"contact_number\": \"1234567890\" \n} "
    },
    {
        "role": "user",
        "content": "Successful JSON body for a POST request to the endpoint Order"
    },
    {
        "role": "assistant",
        "content": "{ \n \"customer\": { \n \"name\": \"John Doe\", \n \"email\": \"johndoe@example.com\", \n \"phone\": \"1234567890\", \n \"address\": \"123 Main St\", \n \"city\": \"Anytown\", \n \"lat\": 40.7128, \n \"lon\": -74.0060 \n }, \n \"lines\": [ \n { \n \"product\": { \n \"name\": \"Product A\", \n \"category\": \"femcare\", \n \"unit_price\": 10.0 \n }, \n \"quantity\": 5 \n }, \n { \n \"product\": { \n \"name\": \"Product B\", \n \"category\": \"grooming\", \n \"unit_price\": 20.0 \n }, \n \"quantity\": 10 \n } \n ] \n}"
    },
    {
        "role": "user",
        "content": "Successful JSON body for a POST request to the endpoint Product"
    },
    {
        "role": "assistant",
        "content": "{ \n \"name\": \"Sample Product\", \n \"raw_materials\": [ \n { \n \"raw_material\": { \n \"name\": \"Product A\", \n \"description\": \"Sample description A\", \n \"type\": \"Type A\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"quantity\": 10 \n },\n {\n \"raw_material\": { \n \"name\": \"Product B\", \n \"description\": \"Sample description B\", \n \"type\": \"Type b\", \n \"unit_of_measurement\": \"unit\" \n }, \n \"quantity\": 30 \n }\n ] \n}"
    },
    {
        "role": "user",
        "content": "I want to run an Analysis"
    },
    {
        "role": "assistant",
        "content": "To run the Analysis I will need the below information\nName\nCountry (should be one of 'United States', 'Canada', 'Poland', 'Germany', 'France')\nStart date\nEnd date\n\nFor at least three products (three or more products are required):\nBrand name\nTarget audience name\nReach\nCost\n\nFor each audience:\nGender flag\nStart age quantity\nEnd age quantity"
    },
    {
        "role": "user",
        "content": "I want to register a Supplier"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the supplier:\nName\nContact Person\nContact Number\n\nFor each raw material:\nName\nDescription\nType\nUnit of measurement\nPrice\nMinimum Order quantity"
    },
    {
        "role": "user",
        "content": "I want to register an Order"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the order:\nRegarding the Customer:\nName\nEmail\nPhone\nAddress\nCity\nLatitude\nLongitude\n\nFor each order line:\nProduct Name\nProduct Category (should be one of: 'femcare', 'babycare', 'grooming', 'healthcare', 'fabriccare', 'homecare')\nProduct Unit Price\nQuantity"
    },
    {
        "role": "user",
        "content": "I want to register a Product"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the product:\nName\n\nFor each raw material that the product requires:\nName\nDescription\nType,\nUnit of measurement\nQuantity"
    },
    {
        "role": "user",
        "content": "I want to register a supplier"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the supplier:\nName\nContact Person\nContact Number\n\nFor each raw material:\nName\nDescription\nType\nUnit of measurement\nPrice\nMinimum Order quantity"
    },
    {
        "role": "user",
        "content": "I want to analyze"
    },
    {
        "role": "assistant",
        "content": "To run the Analysis I will need the below information\nName\nCountry (should be one of 'United States', 'Canada', 'Poland', 'Germany', 'France')\nStart date\nEnd date\n\nFor at least three products (three or more products are required):\nBrand name\nTarget audience name\nReach\nCost\n\nFor each audience:\nGender flag\nStart age quantity\nEnd age quantity"
    },
    {
        "role": "user",
        "content": "Analysis"
    },
    {
        "role": "assistant",
        "content": "To run the Analysis I will need the below information\nName\nCountry (should be one of 'United States', 'Canada', 'Poland', 'Germany', 'France')\nStart date\nEnd date\n\nFor at least three products (three or more products are required):\nBrand name\nTarget audience name\nReach\nCost\n\nFor each audience:\nGender flag\nStart age quantity\nEnd age quantity"
    },
    {
        "role": "user",
        "content": "Supplier"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the supplier:\nName\nContact Person\nContact Number\n\nFor each raw material:\nName\nDescription\nType\nUnit of measurement\nPrice\nMinimum Order quantity"
    },
    {
        "role": "user",
        "content": "Order"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the supplier:\nName\nContact Person\nContact Number\n\nFor each raw material:\nName\nDescription\nType\nUnit of measurement\nPrice\nMinimum Order quantity"
    },
    {
        "role": "user",
        "content": "I want to enter an order"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the supplier:\nName\nContact Person\nContact Number\n\nFor each raw material:\nName\nDescription\nType\nUnit of measurement\nPrice\nMinimum Order quantity"
    },
    {
        "role": "user",
        "content": "Product"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the product:\nName\n\nFor each raw material that the product requires:\nName\nDescription\nType,\nUnit of measurement\nQuantity"
    },
    {
        "role": "user",
        "content": "I want to enter a product"
    },
    {
        "role": "assistant",
        "content": "I will need you to provide me with some information about the product:\nName\n\nFor each raw material that the product requires:\nName\nDescription\nType,\nUnit of measurement\nQuantity"
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
    
    print("ORYGINAL MESSAGE")
    print(response["choices"][0]["message"]["content"])

    try:
        response_text = response["choices"][0]["message"]["content"].split("```")
        data = response_text[1]
        sentence = response_text[0]
        print("ORYGINAL SENTENCE")
        print(sentence)

        if "supplier" in sentence.lower():
            api = "supplier"
        elif "product" in sentence.lower():
            api = "product"
        elif "order" in sentence.lower():
            api = "order"
        elif "analysis" in sentence.lower():
            api = "analysis"

        print(data)
        code = post_request(json.loads(data), api)
        if code == 200:
            print(f"Tell me that {api} was added")

    except Exception as err:
        print(err)
        print("No json")

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
