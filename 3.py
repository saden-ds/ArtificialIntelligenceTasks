import re

text_1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text_2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

def iegut_vardus(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return set(words)

words_text_1 = iegut_vardus(text_1)
words_text_2 = iegut_vardus(text_2)

common_words = words_text_1.intersection(words_text_2)

coincidence_level = len(common_words) / len(words_text_1) * 100

print(f"Kopējie vārdi: {common_words}")
print(f"Sakritības līmenis: {coincidence_level:.2f}%")