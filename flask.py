from flask import Flask, request, jsonify
from ai_model import analyze_design

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    image_path = data['image_path']
    score, feedback = analyze_design(image_path)
    return jsonify(score=score, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
