---

```markdown
# 🧠 Lemmatizer API with FastAPI

This is a simple REST API built using **FastAPI** and **spaCy** to lemmatize English sentences. It accepts raw text input and returns a list of lemmatized words.

---

## 🚀 Features

- Accepts English text via POST request
- Uses spaCy's `en_core_web_sm` model
- Lightweight and runs locally or can be deployed to services like Render

---

## 🧰 Requirements

- Python 3.8 or higher
- Windows OS
- Git (optional for cloning)
- [spaCy](https://spacy.io/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

## 📦 Installation (Windows)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/lemmatizer-api.git
cd lemmatizer-api
```

> If you didn’t clone with Git, just download the ZIP from GitHub and extract it.

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn spacy
python -m spacy download en_core_web_sm
```

---

### 5. Run the server

```bash
uvicorn main:app --reload
```

Server will start at:  
`http://127.0.0.1:8000`

Test endpoint:
- `POST /lemmatize`

---

## 📬 Example Request (via Postman)

**URL:** `http://127.0.0.1:8000/lemmatize`  
**Method:** `POST`  
**Header:** `Content-Type: application/json`  
**Body:**
```json
{
  "text": "She was running towards the cars and playing in the rain."
}
```

**Response:**
```json
{
  "lemmas": ["she", "be", "run", "towards", "the", "car", "and", "play", "in", "the", "rain", "."]
}
```

---

## 🌐 Deployment

To deploy this API online (e.g., Render.com), refer to the [deployment guide](#) or use the provided `render.yaml` file.

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
```

---
