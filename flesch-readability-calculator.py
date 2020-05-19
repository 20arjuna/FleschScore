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

@app.route('/')
def hello():
    return render_template('frontend.html')

@app.route('/mainlocal', methods=['POST'])
def main():
    print("in the main method")
    text = request.form.get("textInput", 0)
    words = len(text.split())
    sentences = text.count(".")

    syllables = 0

    for word in text.split():
        syllables+= syllable_count(word)

    score = calculate_score(words, sentences, syllables)

    print("words: " + str(words) + "\n")
    print("sentences: " + str(sentences) + "\n")
    print("syllables: " + str(syllables) + "\n")

    print("score: " + str(round(score, 1)))

    # outputFile = open("data.txt", "a")
    # outputFile.write(str(round(score, 1)))
    # outputFile.close()

    return '<h1>' + str(round(score, 1)) + '</h1>'
