from fastapi import FastAPI
from pydantic import BaseModel

class EmailRequest(BaseModel):
    texto_email: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Servidor AutoU no ar!"}

@app.post("/processar-email")
async def processar_email(request: EmailRequest):
    texto_recebido = request.texto_email

    return {
        "texto_recebido": texto_recebido,
        "categoria": "Produtivo (Simulado)",
        "resposta_sugerida": "Esta é uma resposta automática simulada. Obrigado pelo contato! (Simulado)"
    }