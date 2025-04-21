import streamlit as st
import requests

# Konfigurasi URL Backend
BACKEND_URL = "http://127.0.0.1:5000"

st.title("📄 AI Resume Analyzer")
st.write("Upload 1 atau lebih CV dan bandingkan dengan job requirements.")

# Input Job Description
job_desc = st.text_area("Masukkan Job Description", height=150)

# Upload file (multiple PDF)
uploaded_files = st.file_uploader("Upload CV (PDF)", type=["pdf"], accept_multiple_files=True)

if st.button("Analyze") and uploaded_files:
    if not job_desc:
        st.error("Harap masukkan job description!")
    else:
        files = [('files', (file.name, file, 'application/pdf')) for file in uploaded_files]
        response = requests.post(f"{BACKEND_URL}/upload", files=files, data={"job_desc": job_desc})

        if response.status_code == 200:
            results = response.json().get("extracted_texts", {})
            for filename, data in results.items():
                st.subheader(f"📂 {filename}")
                st.write(f"🌍 **Detected Language:** `{data['language']}`")
                st.write(f"✅ **Match Score:** `{data['match_score']}%`")
                st.text_area("Extracted Text:", data['text'], height=300)
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")

# import streamlit as st
# import requests

# # Konfigurasi URL Backend
# BACKEND_URL = "http://127.0.0.1:5000"

# st.title("📄 AI Resume Analyzer")
# st.write("Upload 1 atau lebih CV untuk diekstrak teksnya.")

# # Input file (multiple PDF)
# uploaded_files = st.file_uploader("Upload CV (PDF)", type=["pdf"], accept_multiple_files=True)

# if st.button("Analyze") and uploaded_files:
#     files = [('files', (file.name, file, 'application/pdf')) for file in uploaded_files]
#     response = requests.post(f"{BACKEND_URL}/upload", files=files)

#     if response.status_code == 200:
#         results = response.json().get("extracted_texts", {})
#         for filename, data in results.items():
#             st.subheader(f"📂 {filename}")
#             st.write(f"🌍 **Detected Language:** `{data['language']}`")
#             st.text_area("Extracted Text:", data['text'], height=300)
#     else:
#         st.error(f"Error: {response.json().get('error', 'Unknown error')}")



# # import streamlit as st
# # import requests

# # # Konfigurasi URL Backend
# # BACKEND_URL = "http://127.0.0.1:5000"

# # st.title("📄 AI Resume Analyzer")
# # st.write("Upload 1 atau lebih CV untuk diekstrak teksnya.")

# # # Input file (multiple PDF)
# # uploaded_files = st.file_uploader("Upload CV (PDF)", type=["pdf"], accept_multiple_files=True)

# # if st.button("Analyze") and uploaded_files:
# #     files = [('files', (file.name, file, 'application/pdf')) for file in uploaded_files]
# #     response = requests.post(f"{BACKEND_URL}/upload", files=files)

# #     if response.status_code == 200:
# #         results = response.json().get("extracted_texts", {})
# #         for filename, text in results.items():
# #             st.subheader(f"📂 {filename}")
# #             st.text_area("Extracted Text:", text, height=300)
# #     else:
# #         st.error(f"Error: {response.json().get('error', 'Unknown error')}")
