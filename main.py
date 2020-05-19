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


text = "To measure how each team performed, I'm comparing their roster, cap situation and future draft capital at the beginning of the offseason to what they have in mid-May. The most important thing a team can do is add talent, so those that made significant inroads in improving their roster will rank highly, while those that saw key pieces leave without replacements won't. I also considered how each attacked their specific needs, how well they read the market and handled the financial side of their deals, and what they did to create future draft picks. For each team, I'll include what went right, what went wrong, what they might have done differently with a bit of hindsight and what they need to do next in the months to come. Finally, and this is important: These aren't power rankings of how these teams will perform in 2020. Some of the worst teams in the league from last season will finish at or near the top of these rankings because they were able to draft immediate-impact players at key positions, while some of the best teams shed talent or weren't able to add much in the draft because they had already dealt away picks."

words = len(text.split())
sentences = text.count(".")

syllables = 0

for word in text:
    syllables+= syllable_count(word)

print("words: " + str(words) + "\n")
print("sentences: " + str(sentences) + "\n")
print("syllables: " + str(syllables) + "\n")
