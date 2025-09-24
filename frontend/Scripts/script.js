const emailInput = document.getElementById('email-input');
const analyzeBtn = document.getElementById('analyze-btn');
const loader = document.getElementById('loader');
const resultContainer = document.getElementById('result-container');
const resultCategory = document.getElementById('result-category');
const resultSuggestion = document.getElementById('result-suggestion');

const fileInput = document.getElementById('file-input');

const backendUrl = 'http://127.0.0.1:8000/processar-email';

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (!file) {
        return;
    }

    emailInput.value = "Lendo arquivo...";
    const reader = new FileReader();

    if (file.type === 'text/plain') {
        reader.onload = (e) => {
            emailInput.value = e.target.result;
        };
        reader.readAsText(file);
    }
    else if (file.type === 'application/pdf') {
        reader.onload = (e) => {
            const data = new Uint8Array(e.target.result);
            pdfjsLib.getDocument(data).promise.then((pdf) => {
                let fullText = '';
                const numPages = pdf.numPages;
                let pagesProcessed = 0;

                for (let i = 1; i <= numPages; i++) {
                    pdf.getPage(i).then((page) => {
                        page.getTextContent().then((textContent) => {
                            fullText += textContent.items.map(item => item.str).join(' ') + '\n';
                            pagesProcessed++;
                            if (pagesProcessed === numPages) {
                                emailInput.value = fullText;
                            }
                        });
                    });
                }
            }).catch(console.error);
        };
        reader.readAsArrayBuffer(file);
    } else {
        alert('Formato de arquivo não suportado. Por favor, selecione .txt ou .pdf.');
        emailInput.value = "";
    }

    fileInput.value = '';
});

analyzeBtn.addEventListener('click', async () => {
    const emailText = emailInput.value;

    if (!emailText.trim() || emailText === "Lendo arquivo...") {
        alert('Por favor, cole um texto ou carregue um arquivo válido.');
        return;
    }

    loader.classList.remove('hidden');
    resultContainer.classList.add('hidden');
    analyzeBtn.disabled = true;

    try {
        const response = await fetch(backendUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ texto_email: emailText }),
        });

        if (!response.ok) {
            throw new Error('Houve um problema com a resposta do servidor.');
        }

        const data = await response.json();

        resultCategory.textContent = data.categoria || "N/A";
        resultSuggestion.textContent = data.resposta_sugerida || "N/A";

        resultContainer.classList.remove('hidden');

    } catch (error) {
        console.error('Erro ao analisar o email:', error);
        alert('Não foi possível analisar o email. Tente novamente.');
    } finally {
        loader.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
});