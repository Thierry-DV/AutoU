import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("A chave da API do Gemini não foi encontrada. Verifique seu arquivo .env")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

class EmailRequest(BaseModel):
    texto_email: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Servidor AutoU no ar!"}


@app.post("/processar-email")
async def processar_email(request: EmailRequest):
    try:

        prompt = f"""
            Você é um assistente de IA para uma empresa do setor financeiro.
            Sua tarefa é analisar o email abaixo e retornar APENAS um objeto JSON.

            O email é:
            \"\"\"
            {request.texto_email}
            \"\"\"

            Analise o email e retorne um objeto JSON com duas chaves:
            1. "categoria": classifique o email como "Produtivo" (se requer uma ação ou contém informação importante) ou "Improdutivo" (se for um agradecimento, felicitação ou spam).
            2. "resposta_sugerida": com base na categoria, sugira uma resposta curta e profissional em português. Se for improdutivo e não precisar de resposta, sugira "Nenhuma ação necessária.".
        """

        response = model.generate_content(prompt)

        ia_response_str = response.text.replace("```json", "").replace("```", "").strip()

        json_response = json.loads(ia_response_str)

        return json_response

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        raise HTTPException(status_code=500, detail="Erro ao processar o e-mail com a IA.")