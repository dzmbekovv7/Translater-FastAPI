from transformers import pipeline
from db import get_connection
import torch

translation_pipeline = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")

def translate_and_save(original_text: str) -> str:
    result = translation_pipeline(original_text)
    translated_text = result[0]['translation_text']

    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO translation_history (original_text, translated_text) VALUES (%s, %s)",
            (original_text, translated_text)
        )
    conn.commit()
    conn.close()

    return translated_text
