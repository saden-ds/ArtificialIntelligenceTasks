from transformers import pipeline

# Ielādēt automātiskās rezumēšanas pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Raksts, kuru vēlamies rezumēt
article = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. 
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. 
Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

# Izveidot rezumējumu
summary = summarizer(article, max_length=100, min_length=50, do_sample=False)

# Izvadīt rezumējumu
print("Rezultāts: ", summary[0]['summary_text'])

