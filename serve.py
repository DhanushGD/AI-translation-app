from fastapi import FastAPI, HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes
from langchain_openai import OpenAI
from openai import OpenAI as OpenAI_Client

load_dotenv()

# Load environment variables
Langchain_api = os.environ["LANGSMITH_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
langchain_project = os.environ["LANGSMITH_PROJECT"]
open_ai_api = os.getenv("OPEN_AI_API")
groq_api = os.getenv("GROQ_API_KEY")

# Initialize the models
groq_model = ChatGroq(temperature=0, groq_api_key=groq_api, model_name="llama-3.3-70b-versatile")

# Initialize OpenAI Client
openai_client = OpenAI_Client(api_key=open_ai_api)

# 1. Create a prompt template
generic_template = "Translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages(
    [("system", generic_template), ("user", "{text}")]
)
parser = StrOutputParser()

# 2. Create chain (Groq model by default)
groq_chain = prompt | groq_model | parser

# Initialize FastAPI app
app = FastAPI(title="Langchain server", version="1.0", description="A simple API server using langchain runnable interface")

# 3. Add routes for chain processing
add_routes(app, groq_chain, path="/chain")

# OpenAI API translation function
def openai_translation(text, language):
    prompt = f"Translate the following text to {language}: {text}"
    response = openai_client.completions.create(
        model="gpt-3.5-turbo",  # You can adjust to another OpenAI model like gpt-4
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# 4. Custom route for handling dynamic language requests
@app.post("/chain/invoke")
async def invoke_chain(request: dict):
    # Check if the required fields are present
    if "input" not in request or "language" not in request["input"] or "text" not in request["input"] or "model_type" not in request["input"]:
        raise HTTPException(status_code=400, detail="Invalid input format. 'input.language', 'input.text', and 'input.model_type' are required.")
    
    language = request["input"]["language"]
    text = request["input"]["text"]
    model_type = request["input"]["model_type"]

    # Process the incoming request here (chain invocation, etc.)
    try:
        if model_type == "Groq":
            # Using Groq Model
            response = groq_chain.invoke({"language": language, "text": text})
        elif model_type == "OpenAI":
            # Using OpenAI Model
            response = openai_translation(text, language)
        else:
            raise HTTPException(status_code=400, detail="Invalid model type selected.")
        
        return {"output": response, "metadata": {"run_id": "some-id"}}  # You can add more metadata if necessary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing request: {e}")

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
