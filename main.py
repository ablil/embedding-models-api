from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import os

app = Flask(__name__)

# Load model once at startup (cached if possible)
MODEL_NAME = os.getenv("MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
model = SentenceTransformer(MODEL_NAME)

@app.route("/embed", methods=["POST"])
def embed_text():
    data = request.get_json(silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]
    if isinstance(text, str):
        text = [text]

    embeddings = model.encode(text).tolist()
    return jsonify({"embeddings": embeddings})

@app.route("/health")
def health():
    return {"status": "ok"}