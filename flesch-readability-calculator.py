from flask import Flask,render_template, Response, request, redirect, url_for, send_file

app = Flask(__name__)

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def calculate_score(words, sentences, syllables):
    score = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    return score

def getAnalysis(score):
    if (score <= 30):
        return "Very difficult to read. Professional reading level."
    elif (score <= 50):
        return "Difficult to read. College reading level"
    elif (score <= 60):
        return "Fairly difficult to read. 10th - 12th grade level."
    elif (score <= 70):
        return "Plain English. 8th - 9th grade level."
    elif (score <= 80):
        return "Fairly easy to read. 7th grade reading level."
    elif (score <= 90):
        return "Easy to read. 6th grade reading level."
    elif (score <= 100):
        return "Very easy to read. Kids stuff."


@app.route('/')
def hello():
    return render_template('frontend.html')

@app.route('/mainlocal', methods=['GET','POST'])
def main():
    print("in the main method")
    text = request.form.get("textInput", 0)
    words = len(text.split())
    sentences = text.count(".")

    syllables = 0

    for word in text.split():
        syllables+= syllable_count(word)

    score = calculate_score(words, sentences, syllables)

    analysis = getAnalysis(score)



    return  '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script><style>body {background-color: black;} h1{color: white;display: flex;flex-direction: column;justify-content: center;text-align: center;}img {display: block; margin-left: auto;margin-right: auto;}h4{color: white;display: flex;flex-direction: column;justify-content: center;text-align: center;}</style><h1>' + str(round(score, 1)) + '</h1>' + '<h4>' + analysis + '</h4>'
