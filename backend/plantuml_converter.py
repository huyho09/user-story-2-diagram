import subprocess

def generate_diagram(plantuml_code):
    file_path = "diagram.puml"
    image_path = "diagram.png"
    
    with open(file_path, "w") as file:
        file.write(plantuml_code)
    
    subprocess.run(["plantuml", file_path])
    
    return image_path
