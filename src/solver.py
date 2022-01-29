from flask import Flask, send_from_directory, request, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html', data = ["","","","",""])

@app.route('/', methods=['POST'])
def my_form_post():
    letters_present = request.form['letters_present']
    letters_absent = request.form['letters_absent']
    regex = request.form['regex']
    print(letters_present,letters_absent,regex)


    data = ["Mouse","Train","Solve","Right","Tests"]
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)