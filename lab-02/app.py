from flask import Flask, jsonify, render_template, request

from ciphers import decrypt_caesar, decrypt_playfair, encrypt_caesar, encrypt_playfair

app = Flask(__name__)


def parse_caesar_key(value: str | int | None) -> int:
    try:
        key = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("Khóa Caesar phải là số nguyên từ 0 đến 25.") from exc

    if not 0 <= key <= 25:
        raise ValueError("Khóa Caesar phải nằm trong khoảng 0 đến 25.")
    return key


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/caesar/encrypt")
def caesar_encrypt_api():
    data = request.get_json(silent=True) or {}
    try:
        text = str(data.get("text", ""))
        key = parse_caesar_key(data.get("key"))
        return jsonify({"result": encrypt_caesar(text, key)})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.post("/api/caesar/decrypt")
def caesar_decrypt_api():
    data = request.get_json(silent=True) or {}
    try:
        text = str(data.get("text", ""))
        key = parse_caesar_key(data.get("key"))
        return jsonify({"result": decrypt_caesar(text, key)})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.post("/api/playfair/encrypt")
def playfair_encrypt_api():
    data = request.get_json(silent=True) or {}
    try:
        text = str(data.get("text", ""))
        key = str(data.get("key", ""))
        return jsonify({"result": encrypt_playfair(text, key)})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.post("/api/playfair/decrypt")
def playfair_decrypt_api():
    data = request.get_json(silent=True) or {}
    try:
        text = str(data.get("text", ""))
        key = str(data.get("key", ""))
        return jsonify({"result": decrypt_playfair(text, key)})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(debug=True)
