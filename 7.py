from transformers import BertModel, BertTokenizer
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Ielādējam BERT modeli un tokenizatoru
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Funkcija, lai iegūtu vārdu vektoru no BERT modeļa
def get_word_vector(word):
    inputs = tokenizer(word, return_tensors='pt')
    outputs = model(**inputs)
    # Iegūstam pēdējā slāņa vidējo vektoru
    word_vector = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
    return word_vector

# Vārdi, kuriem vēlamies iegūt vektorus
words = ["māja", "dzīvoklis", "jūra"]

# Iegūstam vektorus katram vārdam
word_vectors = {word: get_word_vector(word) for word in words}
# print('Vardu vektors: ', word_vectors);

# Salīdzinām līdzību starp vārdiem, izmantojot kosinusa līdzību
similarity = {}
for word1, vector1 in word_vectors.items():
    similarity[word1] = {}
    for word2, vector2 in word_vectors.items():
        similarity_score = cosine_similarity([vector1], [vector2])[0][0]
        similarity[word1][word2] = similarity_score

# Izdrukājam rezultātus
for word1, similarities in similarity.items():
    for word2, score in similarities.items():
        print(f"Līdzība starp '{word1}' un '{word2}': {score:.4f}")
