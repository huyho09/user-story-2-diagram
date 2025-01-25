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
    if not data:
        return jsonify({"error": "No user story provided"}), 400
    
    plantuml_code = generate_plantuml(data)
    diagram_url = generate_diagram(plantuml_code)
    return jsonify({"diagram_url": diagram_url})

if __name__ == '__main__':
    app.run(debug=True)
