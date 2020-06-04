def word_count(s):
    table = {}
    ignore_lst = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    s = s.lower()
    for char in s:
        if char in ignore_lst:
            s = s.replace(char, '')
    for word in s.split():
        if word in table:
            table[word]+=1
        else:
            table[word] = 1
    return table

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))