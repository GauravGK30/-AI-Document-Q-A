async function uploadPDF() {
    const fileInput = document.getElementById("pdfFile");
    const status = document.getElementById("uploadStatus");

    if (!fileInput.files.length) {
        alert("Please select a PDF");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    status.innerText = "Uploading...";

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    if (response.ok) {
        status.innerText = "✅ Document uploaded successfully";
    } else {
        status.innerText = "❌ Upload failed";
    }
}

async function askQuestion() {
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");

    if (!question) {
        alert("Enter a question");
        return;
    }

    answerBox.innerText = "Thinking...";

    const response = await fetch(`/ask?query=${encodeURIComponent(question)}`);
    const data = await response.json();

    answerBox.innerText = data.answer || "No answer found";
}
