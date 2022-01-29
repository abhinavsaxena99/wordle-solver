import pandas as pd
import pickle

# Lexipedia 5 letter words (Only Wiktionary words)
# https://en.lexipedia.org/
df = pd.read_csv('en_wikt_words_0_5-5.txt', sep=' ', header = None)

ranked_words = df.iloc[:, 0]. tolist()
ranked_words = [x.upper() for x in ranked_words]

print(len(ranked_words))
print(ranked_words[:100])


with open('src/ranked_words.pkl', 'wb') as f:
    pickle.dump(ranked_words, f)