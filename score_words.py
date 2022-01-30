import pickle
import random

# Optimal words are those which have the max number of unique and most common letters

scores = {
    "E": 11.1607,
    "A": 8.4966,
    "R": 7.5809,
    "I": 7.5448,
    "O": 7.1635,
    "T": 6.9509,
    "N": 6.6544,
    "S": 5.7351,
    "L": 5.4893,
    "C": 4.5388,
    "U": 3.6308,
    "D": 3.3844,
    "P": 3.1671,
    "M": 3.0129,
    "H": 3.0034,
    "G": 2.4705,
    "B": 2.0720,
    "F": 1.8121,
    "Y": 1.7779,
    "W": 1.2899,
    "K": 1.1016,
    "V": 1.0074,
    "X": 0.2902,
    "Z": 0.2722,
    "J": 0.1965,
    "Q": 0.1962
}

ranked_words = []

with open('src/ranked_words.pkl', 'rb') as f:
    ranked_words = pickle.load(f)

def find_score(word):
    score = 0
    taken = set()
    # WHICH
    for c in word:
        if c not in taken:
            taken.add(c)
            score += scores[c]
    score = float("{:.4f}".format(score))
    return score


scored_words = {}

for word in ranked_words:
    scored_words[word] = find_score(word)

print(len(scored_words))

word, score = random.choice(list(scored_words.items()))
print(word,score)
print("STARE",scored_words["STARE"])

with open('src/scored_words.pkl', 'wb') as f:
    pickle.dump(scored_words, f)