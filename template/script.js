document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault(); 

    const formData = new FormData();
    const pdfFile = document.getElementById('pdfFile').files[0];
    formData.append('pdf_file', pdfFile);

    const messageElement = document.getElementById('message');



    const summaryElement = document.getElementById('summary');
    const loadingElement = document.getElementById('loading');
    messageElement.textContent = '';
    summaryElement.textContent = '';
    loadingElement.style.display = 'block';

    try {
        const response = await fetch('http://127.0.0.1:8000/summarize/', {
            method: 'POST',
            body: formData
        });

        loadingElement.style.display = 'none';

        if (!response.ok) {
            throw new Error('Failed to upload PDF');
        }
        const data = await response.json();
        if (data.summaries && Array.isArray(data.summaries)) {
            summaryElement.textContent = data.summaries.join('\n');
        } else {
            summaryElement.textContent = 'No summaries available.';
        }
    } catch (error) {
        loadingElement.style.display = 'none'; 
        messageElement.textContent = `Error: ${error.message}`;
    }
});
