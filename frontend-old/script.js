
document.getElementById("userStoryForm").onsubmit = async function (e) {
    e.preventDefault();  // Prevent default form submission

    // Get input values
    var role = document.getElementById("role").value;
    var want = document.getElementById("want").value;
    var soThat = document.getElementById("soThat").value;
    var criteria = document.getElementById("criteria").value;
    var workflowSteps = document.getElementById("workflowSteps").value;

    // Format the Markdown
    const markdownData = `
A. User Story

[AS A] ${role}

[I WANT] ${want}

[SO THAT] ${soThat}

B. Acceptance Criteria

${criteria}

C. Workflow Steps

${workflowSteps}
    `;

    try {
        // Send the Markdown text to backend API
        const response = await fetch("http://127.0.0.1:5000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ user_story: workflowSteps })
        });

        if (!response.ok) {
            throw new Error("Failed to generate the diagram");
        }

        // Backend returns a JSON response with `markdown_output` and `diagram_url`
        const result = await response.json();

        // Display Markdown Output
        document.getElementById("markdownOutput").innerText = result.markdown_output;

        // Display the Generated Diagram
        document.getElementById("diagramOutput").innerHTML = `<img src="http://127.0.0.1:5000/${result.diagram_url}" alt="Generated Diagram">`;

    } catch (error) {
        console.error("Error:", error);
    }
};
