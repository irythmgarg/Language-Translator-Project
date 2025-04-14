# Language-Translator-Project
🌐 Language Detection and Translation App
A simple and elegant web-based language translator built with Flask, utilizing Natural Language Processing (NLP) tools like langdetect and googletrans to detect and translate text across multiple languages.

📌 Project Overview
Language translation is the process of converting text or speech from one language to another while preserving its meaning and context. This app tackles two core NLP problems:

Language Detection

Language Translation

Built using Python, Flask, and open-source machine learning APIs, this app delivers a responsive interface for real-time detection and translation.

🔍 Problem 1: Language Detection
To determine the language of the given input text, we use the langdetect Python package.

✅ Supports 55 languages

📦 Install with:

bash
Copy
Edit
pip install langdetect
Supported language codes:

bash
Copy
Edit
af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr, hu,
id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl, pt, ro, ru, sk, sl, so,
sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw
🌍 Problem 2: Language Translation
Initially, google_trans_new was considered for translation. However, due to API issues and instability, we use the more reliable:

googletrans==4.0.0-rc1

bash
Copy
Edit
pip install googletrans==4.0.0-rc1
This package:

✅ Supports auto language detection

✅ Free and unlimited

✅ Simple API to translate from source to target languages

🛠️ Tech Stack
Component	Description
Flask	Web framework for Python
langdetect	Language detection from text
googletrans	Text translation using Google Translate
HTML/CSS	Frontend (Bootstrap 4)
🚀 How to Run the App
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/machine-translation-app.git
cd machine-translation-app
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt example:

txt
Copy
Edit
Flask
langdetect
googletrans==4.0.0-rc1
3. Run the Flask App
bash
Copy
Edit
python app.py
Then visit: http://127.0.0.1:5000

✨ Features
🧠 Auto-detects input language

🌍 Translates to over 50 languages

⚡ Fast and responsive UI

📱 Mobile-friendly interface

🖼️ Demo

📂 Project Structure
csharp
Copy
Edit
machine-translation-app/
│
├── app.py                  # Main Flask backend
├── templates/
│   └── index.html          # Frontend HTML
├── static/                 # Optional CSS or JS
└── requirements.txt        # Python dependencies
🤖 Future Enhancements
🔊 Text-to-speech output

🎙️ Voice input with speech recognition

📄 File upload (PDF/DOCX) translation

🌐 Multilingual UI

🙌 Acknowledgements
langdetect

googletrans

Flask

📜 License
This project is open-source and available under the MIT License.
