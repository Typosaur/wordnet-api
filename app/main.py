from fastapi import FastAPI

# requires python -m nltk.downloader omw-1.4
from nltk.corpus import wordnet

app = FastAPI()
pos_labels = {'a': 'adjective', 's': 'adjective', 'r': 'adverb', 'n': 'noun', 'v': 'verb'}

@app.get("/synonyms")
def get_synonyms(word: str):

    synsets = []
    for synset in wordnet.synsets(word):
        synonyms = []
        for lemma in synset.lemma_names():
            if lemma != word:
                synonyms.append(lemma.replace("_", " "))

        synsets.append({
            "pos": synset.pos(),
            "pos_label": pos_labels[synset.pos()],
            "definition": synset.definition(),
            "examples": synset.examples(),
            "synonyms": synonyms
        })

    return {
        "word": word,
        "synsets": synsets
    }
