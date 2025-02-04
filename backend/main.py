from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gpt4o_service import generate_plantuml
from plantuml_converter import generate_diagram
import os


# Set proxy environment variables
os.environ['http_proxy'] = 'http://127.0.0.1:3128'
os.environ['https_proxy'] = 'http://127.0.0.1:3128'

app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers=["Content-Type"])

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json.get("user_story")

    # plantuml_code = generate_plantuml(data)
    # image_path = generate_diagram(plantuml_code)
    # send_file(image_path, mimetype='image/png')

    # # Store the Markdown output to return
    # markdown_output = data  
    # # Generate PlantUML format

    if not data:
        return jsonify({"error": "No user story provided"}), 400
    plantuml_code = generate_plantuml(data)
    if not plantuml_code:
        return jsonify({"error": "Failed to extract valid PlantUML code"}), 500
    # Generate Diagram
    image_path = generate_diagram(plantuml_code)
    print(f'This is image path: {image_path}')
    if not image_path:
        return jsonify({"error": "Failed to generate diagram"}), 500
    return jsonify({
        "markdown_output": data,
        "diagram_url": f"/diagram/{os.path.basename(image_path)}"
    })

@app.route('/diagram/<filename>')
def serve_diagram(filename):
    return send_file(f"results/{filename}", mimetype="image/png")


if __name__ == '__main__':
    app.run(debug=True)

