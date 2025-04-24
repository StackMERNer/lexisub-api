# main.py
from fastapi import FastAPI, Request
import spacy

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

@app.post("/lemmatize")
async def lemmatize(request: Request):
    data = await request.json()
    text = data["text"]
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return {"lemmas": lemmas}
