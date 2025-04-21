from flask import Flask, request, jsonify
import pdfplumber
from langdetect import detect
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Fungsi untuk deteksi bahasa
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# Fungsi untuk menghitung kecocokan antara CV dan Job Description
def calculate_similarity(cv_text, job_desc):
    vectorizer = TfidfVectorizer().fit_transform([cv_text, job_desc])
    similarity = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]
    return round(similarity * 100, 2)  # Konversi ke persen

@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload():
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight request successful"}), 200

    print(f"Received request method: {request.method}")  # Debug

    if 'files' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    job_desc = request.form.get("job_desc", "")
    if not job_desc:
        return jsonify({"error": "No job description provided"}), 400

    files = request.files.getlist('files')
    extracted_texts = {}

    for file in files:
        if file.filename.endswith('.pdf'):
            with pdfplumber.open(file) as pdf:
                text = "\n".join([page.extract_text() or '' for page in pdf.pages])
                language = detect_language(text)
                similarity_score = calculate_similarity(text, job_desc)
                
                extracted_texts[file.filename] = {
                    "text": text,
                    "language": language,
                    "match_score": similarity_score
                }
        else:
            return jsonify({"error": f"Invalid file type: {file.filename}"}), 400

    return jsonify({"extracted_texts": extracted_texts})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# from flask import Flask, request, jsonify
# import pdfplumber
# from langdetect import detect, DetectorFactory

# DetectorFactory.seed = 0  # Supaya hasil deteksi lebih konsisten

# app = Flask(__name__)

# def detect_language(text):
#     try:
#         return detect(text)  # Deteksi bahasa
#     except:
#         return "unknown"

# @app.route('/upload', methods=['POST', 'OPTIONS'])
# def upload():
#     if request.method == 'OPTIONS':
#         return jsonify({"message": "CORS preflight request successful"}), 200

#     print(f"Received request method: {request.method}")  # Debug

#     if 'files' not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     files = request.files.getlist('files')
#     extracted_texts = {}

#     for file in files:
#         if file.filename.endswith('.pdf'):
#             with pdfplumber.open(file) as pdf:
#                 text = "\n".join([page.extract_text() or '' for page in pdf.pages])
#                 language = detect_language(text)  # Deteksi bahasa
#                 extracted_texts[file.filename] = {"text": text, "language": language}
#         else:
#             return jsonify({"error": f"Invalid file type: {file.filename}"}), 400

#     return jsonify({"extracted_texts": extracted_texts})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

# # from flask import Flask, request, jsonify
# # import pdfplumber

# # app = Flask(__name__)

# # @app.route('/upload', methods=['POST', 'OPTIONS'])
# # def upload():
# #     if request.method == 'OPTIONS':
# #         return jsonify({"message": "CORS preflight request successful"}), 200

# #     print(f"Received request method: {request.method}")  # Debug

# #     if 'files' not in request.files:
# #         return jsonify({"error": "No file uploaded"}), 400

# #     files = request.files.getlist('files')
# #     extracted_texts = {}

# #     for file in files:
# #         if file.filename.endswith('.pdf'):
# #             with pdfplumber.open(file) as pdf:
# #                 text = "\n".join([page.extract_text() or '' for page in pdf.pages])
# #                 extracted_texts[file.filename] = text
# #         else:
# #             return jsonify({"error": f"Invalid file type: {file.filename}"}), 400

# #     return jsonify({"extracted_texts": extracted_texts})

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)  # Pastikan pakai port 5000