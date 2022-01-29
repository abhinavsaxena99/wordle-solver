from flask import Flask, send_from_directory, request, render_template
app = Flask(__name__)

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
    letters_present = request.form['letters_present']
    letters_absent = request.form['letters_absent']
    regex = request.form['regex']
    print(letters_present,letters_absent,regex)


    data = {
        "message": "Top Guesses :-",
        "letters_present":letters_present,
        "letters_absent":letters_absent,
        "regex":regex,
        "words": []
    }

    data["words"] = ["MOUSE","TRAIN","SOLVE","RIGHT","TESTS"]
    # data["words"] = ["MOUSE","TRAIN","SOLVE"]
    # data["words"] = ["MOUSE"]
    # data["words"] = []
    
    print(data, data["words"],len(data["words"]))

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