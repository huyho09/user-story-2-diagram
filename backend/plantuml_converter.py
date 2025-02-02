import subprocess
import os
from pathlib import Path

# Define the results directory (where the files will be saved)
RESULTS_DIR = Path(__file__).parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)  # Ensure the results folder exists

def generate_diagram(plantuml_code):
    file_path = RESULTS_DIR / "diagram.puml"  
    image_path = RESULTS_DIR / "diagram.png"

    with open(file_path, "w") as file:
        file.write(plantuml_code)

    # Specify the correct PlantUML path
    # Huy is using MacOS. Should replace with your local path that was installed plantuml
    plantuml_path = "/opt/homebrew/bin/plantuml"

    # Check if the PlantUML path exists
    if not os.path.exists(plantuml_path):
        raise FileNotFoundError(f"PlantUML executable not found at: {plantuml_path}")
    
    # Use subprocess to execute PlantUML
    try:
        subprocess.run([plantuml_path, str(file_path)], check=True)
        if not image_path.exists():
            raise FileNotFoundError("Generated image file not found.")
        print("Diagram generated successfully.")
        return str(image_path)  # Return the absolute image path
    except subprocess.CalledProcessError as e:
        print(f"Error running PlantUML: {str(e)}")
        return None
