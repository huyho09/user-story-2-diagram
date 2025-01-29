import openai
import os
import re
from dotenv import load_dotenv


load_dotenv()

def generate_plantuml(user_story):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai.api_key:
        raise ValueError("OpenAI API key is missing. Please check your .env file.")
    
    #print(f'Check workflow:, {user_story}')

    prompt = f"Convert this workflow to plantuml code activity diagram:\n{user_story}"
    
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
        return "Error: No valid PlantUML code generated."  # Return a fallback string