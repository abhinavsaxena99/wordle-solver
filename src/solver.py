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
        "message": "Top 5 guesses :-",
        "letters_present":letters_present,
        "letters_absent":letters_absent,
        "regex":regex,
        "words": [" "," "," "," "," "]
    }

    data["words"] = ["MOUSE","TRAIN","SOLVE","RIGHT","TESTS"]
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)