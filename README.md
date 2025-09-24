# 🚀 Desafio Prático AutoU - Analisador Inteligente de Emails

![Status](https://img.shields.io/badge/status-concluído-green)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-orange)

Projeto desenvolvido por **Thierry Uchoa de Freitas** como parte do processo seletivo para a vaga de Desenvolvimento na AutoU.

## 🔗 Links

* **Frontend da Aplicação (Live Demo):** `https://autou-hpmw.onrender.com/`
* **Backend da Aplicação:** `https://autou-backend-qej7.onrender.com/`

**Nota:** A aplicação está hospedada no plano gratuito do Render. O primeiro acesso após um período de inatividade pode levar cerca de um minuto para carregar devido à inicialização a frio ('cold start') do servidor.

## 📝 Descrição do Projeto

O objetivo deste projeto foi desenvolver uma aplicação web que utiliza Inteligência Artificial para automatizar a leitura e classificação de emails. A solução classifica os emails em "Produtivo" ou "Improdutivo" e sugere uma resposta automática adequada, otimizando o tempo da equipe e automatizando tarefas manuais.

## ✨ Funcionalidades

* **Classificação de Emails:** A IA analisa o conteúdo do email e o categoriza como `Produtivo` (requer ação) ou `Improdutivo` (não requer ação imediata).
* **Sugestão de Resposta:** Com base na categoria, uma resposta profissional e contextual é gerada pela IA.
* **Interface Web Intuitiva:** Permite a inserção de texto diretamente na interface.
* **Upload de Arquivos:** Suporte para upload de emails nos formatos `.txt` e `.pdf`, com extração automática do texto.

## 🛠️ Tecnologias Utilizadas

### Backend
* **Linguagem:** Python 3
* **Framework:** FastAPI
* **IA (NLP):** API do Google Gemini (Modelo `gemini-1.5-flash-latest`)
* **Servidor de Produção:** Gunicorn com Uvicorn
* **Hospedagem:** Render (Web Service)

### Frontend
* **Estrutura:** HTML5
* **Estilização:** CSS3
* **Interatividade:** JavaScript (Vanilla)
* **Leitura de PDF:** Biblioteca `pdf.js` da Mozilla
* **Hospedagem:** Render (Static Site)

## ⚙️ Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

### Pré-requisitos
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads/)

### Passos
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Thierry-DV/AutoU](https://github.com/Thierry-DV/AutoU)
    cd AutoU
    ```

2.  **Configure e rode o Backend:**
    ```bash
    # Navegue para a pasta do backend
    cd backend

    # Crie e ative um ambiente virtual
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate

    # Instale as dependências
    pip install -r requirements.txt

    # Crie um arquivo .env e adicione sua chave de API
    # Exemplo de conteúdo do .env:
    # GEMINI_API_KEY="sua_chave_aqui"

    # Inicie o servidor
    uvicorn main:app --reload
    ```
    O backend estará rodando em `http://127.0.0.1:8000`.

3.  **Abra o Frontend:**
    * Navegue até a pasta `frontend`.
    * Abra o arquivo `index.html` diretamente no seu navegador.

## 🧠 Justificativa das Decisões Técnicas

* **IA: Engenharia de Prompt vs. Fine-Tuning:** Optei pela abordagem de **Engenharia de Prompt** para controlar o comportamento da IA. Esta técnica é ágil, de baixo custo e extremamente eficaz para guiar modelos poderosos como o Gemini, permitindo definir papéis, tarefas e formatos de saída de forma precisa e flexível, sem a necessidade de um grande volume de dados para treinamento.

* **Remoção do NLTK:** Durante o desenvolvimento, a dependência da biblioteca NLTK para pré-processamento clássico apresentou instabilidades de ambiente. Considerando que o modelo de IA (Gemini) performa de maneira superior com o texto original e contextual, tomei a decisão pragmática de remover essa dependência para garantir a estabilidade e a robustez da entrega final, focando na funcionalidade principal do projeto.
