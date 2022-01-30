import pandas as pd
import pickle

# Lexipedia 5 letter words (Only Wiktionary words)
# https://en.lexipedia.org/
df = pd.read_csv('en_wikt_words_0_5-5.txt', sep=' ', header = None)

ranked_words = df.iloc[:, 0]. tolist()

# Some data points are not correct so filtering here (charaters like É also get through the isalpha filter)
final_list = []

for word in ranked_words:
    if len(word)==5:
        flag = True
        for c in word:
            if 'a'<=c<='z' or 'A'<=c<='Z':
                pass
            else:
                flag = False
                break
        if flag:
            final_list.append(word.upper())




print(len(final_list))
print(final_list[:100])


with open('src/ranked_words.pkl', 'wb') as f:
    pickle.dump(final_list, f)