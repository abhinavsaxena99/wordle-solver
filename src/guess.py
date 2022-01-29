import nltk
import pickle

ranked_words = []

with open('src/ranked_words.pkl', 'rb') as f:
    ranked_words = pickle.load(f)


def find(letters_present, letters_absent, regex):
    return ranked_words[:5]