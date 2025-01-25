function convertToMarkdown() {
    const role = document.getElementById("role").value;
    const want = document.getElementById("want").value;
    const soThat = document.getElementById("soThat").value;
    const criteria = document.getElementById("criteria").value;
    const workflowSteps = document.getElementById("workflowSteps").value;

    const markdown = `
A. User Story

[AS A] ${role}

[I WANT] ${want}

[SO THAT] ${soThat}

B. Acceptance Criteria

${criteria}

C. Workflow Steps

${workflowSteps}
    `;

    document.getElementById("markdownOutput").innerText = markdown;
}

// Submit form data to backend
document.getElementById("userStoryForm").onsubmit = async function (e) {
    e.preventDefault();
    
    const markdownData = document.getElementById("markdownOutput").innerText;
    const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_story: markdownData })
    });

    const result = await response.blob();
    const url = window.URL.createObjectURL(result);
    window.open(url);
};
