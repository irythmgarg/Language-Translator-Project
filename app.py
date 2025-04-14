from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

# Function to detect and translate language
def detect_and_translate(text, target_lang):
    detected_lang = detect(text)
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang).text
    return detected_lang, translated_text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    text = request.form.get('text', '')
    target_lang = request.form.get('target_lang', '')
    translation = ''
    detected_lang = ''

    if text and target_lang:
        detected_lang, translation = detect_and_translate(text, target_lang)

    # Get human-readable language name
    detected_lang_name = LANGUAGES.get(detected_lang, detected_lang)

    return render_template(
        'index.html',
        translation=translation,
        detected_lang=detected_lang_name,
        languages=LANGUAGES,
        input_text=text,
        selected_lang=target_lang
    )

if __name__ == '__main__':
    app.run(debug=True)
