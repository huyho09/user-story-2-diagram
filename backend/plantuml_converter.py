import subprocess
import os

def generate_diagram(plantuml_code):
    file_path = "diagram.puml"
    image_path = "diagram.png"

    with open(file_path, "w") as file:
        file.write(plantuml_code)

    # Specify the correct PlantUML path
    # Huy is using MacOS. Should replace with your local path that was installed plantuml
    plantuml_path = "/opt/homebrew/bin/plantuml"

    # Check if the PlantUML path exists
    if not os.path.exists(plantuml_path):
        raise FileNotFoundError(f"PlantUML not found at: {plantuml_path}")

    # Use subprocess to execute PlantUML
    try:
        subprocess.run([plantuml_path, file_path], check=True)
        print("Diagram generated successfully.")
        return image_path
    except subprocess.CalledProcessError as e:
        print(f"Error running PlantUML: {str(e)}")
        return None
