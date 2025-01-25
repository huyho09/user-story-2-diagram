import subprocess
import os
import requests
import urllib.parse
from plantuml import PlantUML, PlantUMLHTTPError

def generate_diagram(plantuml_code):
    base_url = "http://www.plantuml.com/plantuml/png/"
    encoded_code = urllib.parse.quote(plantuml_code)
    full_url = f"{base_url}{encoded_code}"

    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            print("Diagram generated successfully:", full_url)
            return full_url
        else:
            print(f"Error: HTTP {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")
        return None