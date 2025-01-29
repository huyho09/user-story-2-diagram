function convertToMarkdown() {
    let role = document.getElementById("role").value;
    let want = document.getElementById("want").value;
    let soThat = document.getElementById("soThat").value;
    let criteria = document.getElementById("criteria").value;
    let workflowSteps = document.getElementById("workflowSteps").value;

    const markdown = `
        A. User Story

        [AS A] ${role}

        [I WANT] ${want}

        [SO THAT] ${soThat}

        B. Acceptance Criteria

        ${criteria}

        C. Workflow Steps

        ${workflowSteps}`;

    document.getElementById("markdownOutput").innerText = markdown;
}

var workflow = document.getElementById("workflowSteps").value;

// Submit form data to backend
document.getElementById("userStoryForm").onsubmit = async function (e) {
    e.preventDefault();
    
    // const markdownData = document.getElementById("markdownOutput").innerText;
    // const response = await fetch("http://127.0.0.1:5000/generate", {
    //     method: "POST",
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify({ user_story: markdownData })
    // });
    var workflow = document.getElementById("workflowSteps").value;
    // TO DO: using Workflow instead of the whole flow replace markdownData to workflowSteps
    const markdownData = document.getElementById("markdownOutput").innerText;
    const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_story: workflow })
    });

    const result = await response.blob();
    const url = window.URL.createObjectURL(result);
    window.open(url);
};
