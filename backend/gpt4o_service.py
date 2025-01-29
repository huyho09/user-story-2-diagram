import openai
import os
import re
from dotenv import load_dotenv


load_dotenv()

def generate_plantuml(user_story):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai.api_key:
        raise ValueError("OpenAI API key is missing. Please check your .env file.")

    prompt = f"Convert this user story to a PlantUML workflow diagram:\n{user_story}"
    
    # Using new syntax from openai library
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    full_response = response.choices[0].message.content
    # Extract code block from response using regex
    match = re.search(r"```(?:plantuml|uml)?\n(.*?)```", full_response, re.DOTALL)

    if match:
        return match.group(1).strip()  # Extracted code block
    else:
        print("No code block found in the response.")
        return None  # Return None explicitly if no code block is found