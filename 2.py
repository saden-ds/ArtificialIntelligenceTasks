import langid

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

print("Teksta valodas noteikšana:")
for text in texts:
    lang, confidence = langid.classify(text)
    print(f"Teksts: '{text}'")
    print(f"Valoda: {lang}")