import google.generativeai as genai
import os

# Configure your API key (ensure this is in your .env file!)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_design_from_prompt(prompt: str):
    # Using the model for design ideation
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = await model.generate_content_async(
        f"Create a detailed visual description of a fashion design base material based on this request: {prompt}"
    )
    return response.text