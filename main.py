from fastapi import FastAPI
from pydantic import BaseModel
from middleware import setup_cors
from translation import translate_and_save

app = FastAPI()

setup_cors(app)

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TranslationRequest):
    translated_text = translate_and_save(req.text)
    return {"translated_text": translated_text}
