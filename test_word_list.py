import pickle
from nltk.corpus import words

all_words = []
ranked_words = []

all_words = [word.upper() for word in words.words() if len(word)==5]

with open('src/ranked_words.pkl', 'rb') as f:
    ranked_words = pickle.load(f)

count = 0

for word in all_words:
    if word not in ranked_words:
        print(word)
        count+=1

print(count)