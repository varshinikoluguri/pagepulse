alert("JavaScript Loaded");

async function analyzeWebsite() {

    const url = document.getElementById("url").value;
    const result = document.getElementById("result");

    result.innerHTML = "Analyzing...";

    try {

        const response = await fetch(
    https://pagepulse-du14.onrender.com/analyze?url=${encodeURIComponent(url)}
);
        const data = await response.json();

        if (data.error) {
            result.innerHTML = `<p>${data.error}</p>`;
            return;
        }

        result.innerHTML = `
            <h3>Analysis Result</h3>
            <p><b>Status:</b> ${data.status}</p>
            <p><b>Response Time:</b> ${data.response_time_ms} ms</p>
            <p><b>Title:</b> ${data.title}</p>
            <p><b>Meta Description:</b> ${data.meta_description}</p>
            <p><b>H1 Count:</b> ${data.h1_count}</p>
            <p><b>Images Without Alt:</b> ${data.images_without_alt}</p>
            <p><b>Word Count:</b> ${data.word_count}</p>
        `;

    } catch (error) {
        console.error(error);
        result.innerHTML = '<p>Unable to connect to backend.</p>';
    }
}
