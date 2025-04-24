from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

# Define expected request body
class LemmaRequest(BaseModel):
    text: str

@app.post("/lemmatize")
async def lemmatize(payload: LemmaRequest):
    try:
        doc = nlp(payload.text)
        lemmas = [token.lemma_ for token in doc]
        return {"lemmas": lemmas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
