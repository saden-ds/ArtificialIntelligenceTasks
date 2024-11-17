import re


text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def clean_text(text):
    text = re.sub(r'@\w+|http\S+|#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = ' '.join(text.split())

    return text


cleaned_text = clean_text(text)

print("Tīrs teksts:", cleaned_text)
