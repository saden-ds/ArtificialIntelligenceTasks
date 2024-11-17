from googletrans import Translator

# Izveidojiet tulkotāju
translator = Translator()

# Latviešu valodā teikumi
latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

# Tulkot teikumus uz angļu valodu
for text in latvian_texts:
    translation = translator.translate(text, src='lv', dest='en')
    print(f"Latviešu: {text}")
    print(f"Angļu: {translation.text}\n")
