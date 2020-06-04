import random
import re
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()
table = {}
for i, word in enumerate(words):
    if word in table:
        table[word].append(words[i+1])
    else:
        try:
            table[word] = [words[i+1]]
        except:
            pass
start_words = [w for w in table if w[0].isupper() or (w[0]=='"' and w[1].isupper())]
stop_words = [w for w in table if w.endswith(('.', '."', '?', '?"', '!', '!"'))]
for i in range(5):
    word = random.choice(start_words)
    s = word
    while word:
        word = random.choice(table[word])
        s = s + " " + word
        if word in stop_words:
            break
    print(s)
