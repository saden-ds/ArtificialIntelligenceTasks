import spacy

# Load a transformer-based model
nlp = spacy.load("en_core_web_trf")  # Try multilingual models if available

# Latvian text
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

# Process the text
doc = nlp(text)

# Print the recognized entities
for ent in doc.ents:
    if ent.label_ == 'PERSON':  # Personvārds
        print(f"Personvārds: {ent.text}")
    elif ent.label_ == 'ORG':  # Organizācija
        print(f"Organizācija: {ent.text}")
