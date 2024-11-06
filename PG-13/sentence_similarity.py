import spacy
nlp = spacy.load('en_core_web_md')
sentence1 = nlp("The quick brown fox jumps over the lazy dog.")
sentence2 = nlp("The fast brown fox leaps over the lazy dog.")
similarity = sentence1.similarity(sentence2)
print(similarity)  # Close to 1 indicates high similarity
