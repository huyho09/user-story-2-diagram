from flask import Flask, request, jsonify, send_file
from gpt4o_service import generate_plantuml
from plantuml_converter import generate_diagram
import os

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json.get("user_story")
    plantuml_code = generate_plantuml(data)
    image_path = generate_diagram(plantuml_code)
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
