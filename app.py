from flask import Flask, render_template, request, send_file
import os
from encryption import encrypt, decrypt

app = Flask(__name__)
os.makedirs("files", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()
    encrypted = encrypt(data)

    with open("files/" + file.filename + ".enc", "wb") as f:
        f.write(encrypted)

    return "File uploaded & encrypted successfully"

@app.route("/download/<name>")
def download(name):
    with open("files/" + name, "rb") as f:
        encrypted = f.read()

    decrypted = decrypt(encrypted)

    output = "files/decrypted_" + name.replace(".enc", "")
    with open(output, "wb") as f:
        f.write(decrypted)

    return send_file(output, as_attachment=True)

app.run(debug=True)
