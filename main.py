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

text = "The color of animals is by no means a matter of chance; it depends on many considerations, but in the majority of cases tends to protect the animal from danger by rendering it less conspicuous. Perhaps it may be said that if coloring is mainly protective, there ought to be but few brightly colored animals. There are, however, not a few cases in which vivid colors are themselves protective. The kingfisher itself, though so brightly colored, is by no means easy to see. The blue harmonizes with the water, and the bird as it darts along the stream looks almost like a flash of sunlight."

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
