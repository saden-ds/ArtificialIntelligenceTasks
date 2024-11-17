import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('punkt_tab')


text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

text = text.lower()

words = word_tokenize(text)


words = [word for word in words if word.isalnum()]

word_frequency = Counter(words)

print("Vārdu biežuma analīze:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")