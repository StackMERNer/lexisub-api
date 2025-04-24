On **Windows**, here’s exactly where and how to run the `python -m venv venv` command and set up your Python lemmatizer server:

---

## ✅ Step-by-Step on Windows

### **1. Open Command Prompt**
- Press **Win + R**, type `cmd`, and press **Enter**.
- You’ll see the black terminal window.

### **2. Create a Project Folder**
In the terminal:
```bash
mkdir lemmatizer-api
cd lemmatizer-api
```

### **3. Create a Virtual Environment**
Still in the `lemmatizer-api` folder:
```bash
python -m venv venv
```

- This creates a folder named `venv` that contains a local Python environment.

### **4. Activate the Virtual Environment**
```bash
venv\Scripts\activate
```

You should now see something like this in your prompt:
```
(venv) C:\Users\YourName\lemmatizer-api>
```

---

### **5. Install the Required Packages**
```bash
pip install fastapi uvicorn spacy
python -m spacy download en_core_web_sm
```

---

### **6. Create the API Code**
1. Open **Notepad** or a code editor like **VS Code**.
2. Paste this code:

```python
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
```

3. Save it as `main.py` inside the `lemmatizer-api` folder.

---

### **7. Run the Server**
Back in the same Command Prompt:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

You should see something like:
```
Uvicorn running on http://127.0.0.1:8000
```

Your API is now live on your machine. Ready for React Native to connect.

---

Let me know if you want help exposing it to the internet (for mobile access) using services like [ngrok](https://ngrok.com/) or deployment platforms like Render.