import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Servidor AutoU no ar!"}

@app.post("/processar-email")
async def processar_email(request: EmailRequest):
    try:
        prompt = f"""
            Você é um assistente de IA para uma empresa do setor financeiro. Sua tarefa é analisar o email abaixo e retornar APENAS um objeto JSON.
            O email para análise é:
            \"\"\"{request.texto_email}\"\"\"

            Analise o email e retorne um objeto JSON com duas chaves:
            1. "categoria": classifique como "Produtivo" ou "Improdutivo".
            2. "resposta_sugerida": sugira uma resposta curta e profissional em português. Se não precisar de resposta, sugira "Nenhuma ação necessária.".
        """
        response = model.generate_content(prompt)
        ia_response_str = response.text.replace("```json", "").replace("```", "").strip()
        json_response = json.loads(ia_response_str)

        return json_response

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        raise HTTPException(status_code=500, detail="Erro ao processar o e-mail com a IA.")