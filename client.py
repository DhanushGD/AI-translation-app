import streamlit as st
import requests

def get_groq_response(input_text, language, model_type):
    json_body = {
        "input": {
            "language": language,  # Use the selected language
            "text": input_text,
            "model_type": model_type  # Send the model type in the request
        },
        "config": {},
        "kwargs": {}
    }

    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)

    if response.status_code == 200:
        # Extract only the 'output' field from the response
        response_data = response.json()
        return response_data.get("output", "No translation found.")  # Default message if 'output' is not found
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit app
st.title("LLM Language Translator Application")

# Input fields
selected_language = st.text_input("Enter the target language (e.g., French, Spanish, etc.):")

# Model selection dropdown
model_choice = st.selectbox(
    "Choose the translation model:",
    ["Groq", "OpenAI"]  # Add more models if necessary
)

# Upload file section
uploaded_file = st.file_uploader("Upload a text file", type="txt")

if uploaded_file is not None:
    # Read the uploaded file content
    file_content = uploaded_file.read().decode("utf-8")
    
    # Translate the content
    if selected_language:
        translated_text = get_groq_response(file_content, selected_language, model_choice)
        
        # Display translated text
        st.write(f"Translated text: {translated_text}")
        
        # Provide an option to download the translated content
        st.download_button(
            label="Download Translated File",
            data=translated_text,
            file_name="translated_file.txt",
            mime="text/plain"
        )
