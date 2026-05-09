from typing import Any
from flask import Flask, request, jsonify
from src.functional import format_text

app = Flask(__name__)


@app.route("/format", methods=["POST"])
def format_endpoint() -> Any:
    data = request.get_json()
    text = data.get("text", "")
    style = data.get("style", "upper")
    try:
        result = format_text(text, style)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
