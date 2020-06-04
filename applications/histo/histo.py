with open('robin.txt') as f:
    words = f.read()

punct = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
words = words.lower()
for char in words:
    if char in punct:
        words = words.replace(char, '')

hist = {}
for word in words.split():
    if word in hist:
        hist[word] += '#'
    else:
        hist[word] = '#'
maxlen = 0
for word in hist:
    if len(word)>maxlen:
        maxlen = len(word)

for i in sorted(hist.items(), key=lambda a: (-len(a[1]),a[0])):
    print(f'{i[0]:{maxlen}}  {i[1]}')