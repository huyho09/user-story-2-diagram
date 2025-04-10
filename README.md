# User Story Workflow Diagram Generator

## Project Description

This project is a web application that allows users to create user stories and workflows following a structured format. The application simplifies the process of generating diagrams for user stories by leveraging GPT-4o to produce PlantUML code and visual representations.

### Features
1. **User Story Input Form**:
   - A form-based interface for users to input user stories and acceptance criteria.
   - Follows a structured template:
     ```
     A. User Story
     [AS A] <Role>
     [I WANT] ...
     [SO THAT] ...

     B. Acceptance Criteria
     [ACCEPT-1]: ...
     [ACCEPT-2]: ...
     [ACCEPT-3]: ...

     C. Workflow Steps
     Text Editor
     ```
   - Fields for `AS A`, `I WANT`, and `SO THAT` are text inputs.
   - A text editor for workflow steps.

2. **Markdown Conversion**:
   - A button to convert the input into Markdown or plain text.

3. **Backend Integration**:
   - A button to submit the form and send data to a Python-based backend API.

4. **Diagram Generation**:
   - Backend API processes the input, calls GPT-4o to generate PlantUML format, and converts it into a diagram image.

---

## Implementation Details

### Frontend
1. **Technologies**: Bootstrap, HTML, JavaScript, CSS.
2. **Form Elements**:
   - User-friendly form with validation for user story inputs.
   - Rich text editor (e.g., TinyMCE or QuillJS) for Workflow Steps.

3. **Buttons**:
   - ~"Convert to Markdown": Converts form input to Markdown or plain text format.~
   - "Submit": Sends the input data to the backend API.

---

### Backend
1. **Technologies**: Python, Flask/FastAPI.
2. **API Workflow**:
   - Receive user story data in JSON format.
   - Convert data to Markdown format.
   - Use GPT-4o to generate PlantUML code based on the input.
   - Use PlantUML or Graphviz libraries to convert PlantUML text into a diagram image.
   - Respond with the generated diagram image or provide a link to download it.

3. **Endpoints**:
   - `/convert`: Converts form data to Markdown.
   - `/generate-diagram`: Processes user input and returns the generated diagram.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for frontend dependency management)
- PlantUML installed locally or hosted online. You can find the link [here](https://plantuml.com/download)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/huyho09/user-story-2-diagram.git
   cd user-story-2-diagram

2. Install backend dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the backend server:
    ```bash
    python backend/main.py

4. Open the `frontend/index.html` in a browser to access the application.

---
## To Do
- ~Remove Bot comment in the `diagram.puml`. We only need the code to send to GPT-4o~
- ~Check for the issue of `diagram.png`. The image should be displayed.~
- ~Allow all CORS block~
- ~Proxy config~
- ~Remove "Convert to Markdown button" and Markdown output~
- ~Submit button only send the Workflow Steps~
- ~Replace submit type button, using ajax call to avoid the page reload when the source code is changed.~
- Define a project external path to save the source code to avoid page reload
- (Optional) Implement a frontend framework.