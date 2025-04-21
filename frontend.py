import requests

BACKEND_URL = "http://127.0.0.1:5000"  # Pastikan port sesuai

files = {'files': open('cv.pdf', 'rb')}  
response = requests.post(f"{BACKEND_URL}/upload", files=files)

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.text}")  # Cek hasil ekstraksi teks


# import streamlit as st
# import requests
# import tempfile

# # URL Backend Flask
# BACKEND_URL = "http://127.0.0.1:5000"
# st.title("📄 PDF to Text Extractor")

# uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# if uploaded_file is not None:
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
#         temp_file.write(uploaded_file.getvalue())
#         temp_path = temp_file.name

#     files = {"file": open(temp_path, "rb")}
#     response = requests.post(f"{BACKEND_URL}/upload", files=files)
    
#     if response.status_code == 200:
#         extracted_text = response.json().get("text", "")
#         download_url = response.json().get("download_url", "")

#         st.text_area("Extracted Text", extracted_text, height=300)

#         if download_url:
#             st.markdown(f"[⬇ Download Text File]({BACKEND_URL}{download_url})", unsafe_allow_html=True)
#     else:
#         st.error("Failed to process the PDF")
