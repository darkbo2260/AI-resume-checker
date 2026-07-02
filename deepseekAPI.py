import sqlite3
import os
import json as json_lib

from flask import Flask, render_template, request, jsonify
import requests
from PyPDF2 import PdfReader

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("records.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()
api_key = os.environ.get("DEEPSEEK_API_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        text = text.encode('utf-8', errors='ignore').decode('utf-8')

    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        },
        data=json_lib.dumps({
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": f"分析这份简历，指出优缺点和改进建议：{text}"}]
        }).encode('utf-8')
    )
    result = response.json()["choices"][0]["message"]["content"]
    conn = sqlite3.connect("records.db")
    conn.execute("INSERT INTO records (filename, result) VALUES (?, ?)",
                 (file.filename, result))
    conn.commit()
    conn.close()
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
