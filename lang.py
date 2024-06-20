!pip install deep-translator

from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated

tt = input("Enter the text you want to translate: ")
tl = input("Enter the target language ('fr' for French, 'ar' for Arabic): ")

translated_t = translate_text(tt, tl)
print("Translated text:", translated_t)