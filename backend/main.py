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
    return send_file(image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)

