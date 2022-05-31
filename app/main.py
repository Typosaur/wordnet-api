import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# requires python -m nltk.downloader omw-1.4
from nltk.corpus import wordnet

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('CORS_ORIGIN', '*'),
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

pos_labels = {'a': 'adjective', 's': 'adjective', 'r': 'adverb', 'n': 'noun', 'v': 'verb'}

@app.get("/synonyms")
def get_synonyms(word: str):

    terms = []
    for term in wordnet.synsets(word):
        synonyms = []
        for lemma in term.lemma_names():
            if lemma != word:
                synonyms.append(lemma.replace("_", " "))

        terms.append({
            "pos": term.pos(),
            "pos_label": pos_labels[term.pos()],
            "definition": term.definition(),
            "examples": term.examples(),
            "synonyms": synonyms
        })

    return {
        "word": word,
        "terms": terms,
        "license": "https://wordnet.princeton.edu/license-and-commercial-use"
    }
