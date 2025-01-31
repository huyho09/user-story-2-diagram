from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gpt4o_service import generate_plantuml
from plantuml_converter import generate_diagram
import os
from plantuml import PlantUML, PlantUMLHTTPError

app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers=["Content-Type"])

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json.get("user_story")
    plantuml_code = generate_plantuml(data)
    image_path = generate_diagram(plantuml_code)
    send_file(image_path, mimetype='image/png')
    if not data:
        return jsonify({"error": "No user story provided"}), 400
    # Store the Markdown output to return
    markdown_output = data  
    # Generate PlantUML format
    plantuml_code = generate_plantuml(data)
    if not plantuml_code:
        return jsonify({"error": "Failed to extract valid PlantUML code"}), 500
    # Generate Diagram
    image_path = generate_diagram(plantuml_code)
    if not image_path:
        return jsonify({"error": "Failed to generate diagram"}), 500
    return jsonify({
        "markdown_output": markdown_output,
        "diagram_url": image_path  # Path to the image file
    })
@app.route('/diagram.png')
def serve_diagram():
    return send_file("diagram.png", mimetype="image/png")


if __name__ == '__main__':
    app.run(debug=True)

