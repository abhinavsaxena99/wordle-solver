import nltk
import pickle

scored_words = {}
ranked_words = []

with open('src/ranked_words.pkl', 'rb') as f:
    ranked_words = pickle.load(f)

with open('src/scored_words.pkl', 'rb') as f:
    scored_words = pickle.load(f)


print(len(ranked_words))
print(len(scored_words))


def find(letters_present, letters_absent, regex):

    final_list = []
    
    
    
    # Basically when just 2 guesses are remaining, disregard word scores and recommend most common
    # Can ask this from user or infer from length of list
    if len(final_list) < 2:
        pass
    else:
        final_list = sorted(final_list, key = lambda x: (scored_words[x],x), reverse = True)


    if len(final_list) > 5:
        return final_list[:5]
    
    return final_list