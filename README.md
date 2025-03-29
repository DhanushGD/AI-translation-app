# LinguaFlow: AI-Powered Language Translation App

**LinguaFlow** is an AI-driven language translation platform that offers seamless translation services for both text and file content. Built with **Langserve**, **LangChain Groq**, **Langsmith**, and **Streamlit**, it provides powerful AI models like **Groq** and **OpenAI** for translating content into multiple languages.

## Features

- 🗣️ **AI-Powered Translation**: Translates content into multiple languages with Groq and OpenAI models.
- 📂 **File Upload & Translation**: Supports uploading and translating text files for a hassle-free experience.
- 💬 **Language Selection**: Users can select the desired language for translation, streamlining the process.
- 📥 **Download Translated Files**: After translation, users can download the translated content with a single click.
- ⚙️ **Versatile Model Support**: Choose between Groq and OpenAI translation models for tailored results.
- 🔄 **Model Chaining via LCEL**: Use LangChain Expression Language (LCEL) for efficient and advanced model chaining, enabling more complex translation workflows.
- 🔍 **Langsmith Integration**: Track, optimize, and improve LLM workflows with **Langsmith** for real-time insights.

## Installation

To set up and run **LinguaFlow**, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/DhanushGD/AI-translation-app.git
cd AI-translation-app
```
### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```
### Dependencies include:
    - Langserve for serving AI models.
    - LangChain and Groq for language model integration.
    - Streamlit for building the user interface.
    - FastAPI (via Langserve) for serving API endpoints.
    - Langsmith for tracking and optimizing workflows.

### 3. Set Up Environment Variables:
Create a .env file and add the following environment variables:
```bash
LANGSMITH_API_KEY=your_langchain_api_key
OPEN_AI_API=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

### 4. Run the App
To start the LinguaFlow app, run the following command:
```bash
uvicorn serve:app --reload
streamlit run client.py
```
Your app will be available at http://localhost:8501.

## Impact
- **Bridging Language Barriers** 🌍  
  LinguaFlow helps break down language barriers by providing an easy way to translate text and documents across various languages.

- **Enhanced Efficiency** 💼  
  Automates the translation of files and text, saving users time and ensuring consistent translations.

- **Seamless Experience** 🚀  
  Provides a user-friendly interface powered by Streamlit, making it easy for anyone to translate text or upload files for fast translation.

## Tech Stack
- 🐍 Python
- 🌐 Langserve (built on FastAPI)
- 🤖 LangChain & Groq
- 🦙 OpenAI
- 💻 Streamlit
- 🔄 Langsmith
- 🧩 LCEL (LangChain Expression Language)

## App and Langsmith Tracing
Here are two images to give you an overview of the application and how **Langsmith** tracks and optimizes the models used for translation.

*Above: The user interface of the LinguaFlow app, where you can input text or upload a file for translation.*
![Screenshot 2025-03-29 151903](https://github.com/user-attachments/assets/a5f1d08d-a1e8-4d8d-9b90-f9ee3e937e45)

![Screenshot 2025-03-29 152227](https://github.com/user-attachments/assets/ff62f18c-7d34-4258-a788-daf9961bbe2d)
*Above: Langsmith tracing interface that tracks the performance and workflow of the translation models, providing real-time insights.*
