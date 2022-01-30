from flask import Flask, send_from_directory, request, render_template
import pickle
import regex as re

app = Flask(__name__)


scored_words = {}
ranked_words = []

with open('src/ranked_words.pkl', 'rb') as f:
    ranked_words = pickle.load(f)

with open('src/scored_words.pkl', 'rb') as f:
    scored_words = pickle.load(f)


def find(letters_present, letters_absent, regex_string):

    letters_absent = set(letters_absent)
    letters_present = set(letters_present)

    list_without_absents = [word for word in ranked_words if not letters_absent&set(word)]
    
    if len(list_without_absents) == 0:
        return []
    
    list_with_presents = [word for word in list_without_absents if len(letters_present&set(word))==len(letters_present)]
    if len(list_with_presents) == 0:
        list_with_presents = list_without_absents
    
    regex_string = regex_string.replace('-','.')
    regex_string = regex_string.replace('_','.')

    print(regex_string)

    r = re.compile(regex_string)
    final_list = list(filter(r.match,list_with_presents))

    if len(final_list)==0:
        return []
    
    common_word = final_list[0]
    
    # Only choose from 20 most common words
    final_list = final_list[:min(20,len(final_list))]

    # Basically when just 2 guesses are remaining, disregard word scores and recommend most common
    # Can ask this from user or infer from length of list

    if len(final_list) < 15:
        pass
    else:
        final_list = sorted(final_list, key = lambda x: float("{:.4f}".format(scored_words[x])), reverse = True)


    if len(final_list) > 5:
        final_list = final_list[:5]
    
    for x in final_list:
        print(x,scored_words[x])

    if len(final_list) > 0 and common_word not in final_list:
        final_list[-1] = common_word
    
    return final_list

@app.route("/")
def homepage():
    data = {
        "message": "Good starting words :-",
        "letters_present":"",
        "letters_absent":"",
        "regex":"",
        "words": ["STARE","TEARS","RIOTS","CHAIR","EARTH"]
    }
    return render_template('index.html', data = data)

@app.route('/', methods=['POST'])
def my_form_post():
    letters_present = request.form['letters_present'].upper()
    letters_absent = request.form['letters_absent'].upper()
    regex = request.form['regex'].upper()
    print(letters_present,letters_absent,regex)


    data = {
        "message": "Top Guesses :-",
        "letters_present":letters_present,
        "letters_absent":letters_absent,
        "regex":regex,
        "words": []
    }

    # data["words"] = ["MOUSE","TRAIN","SOLVE","RIGHT","TESTS"]
    # data["words"] = ["MOUSE","TRAIN","SOLVE"]
    # data["words"] = ["MOUSE"]
    # data["words"] = []
    
    # print(data, data["words"],len(data["words"]))

    data["words"] = find(letters_present,letters_absent,regex)
    
    
    words_length = len(data["words"])

    if words_length == 1:
        data["message"] = "The word is :-"

    if words_length == 0:
        data["message"] = "Error! re-check the fields"

    # Forcefully make length of data["words"] to 5 always to ensure position of footer (hack)
    for i in range(0,5-words_length):
        data["words"].append("\xa0")
    
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)