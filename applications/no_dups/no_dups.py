def no_dups(s):
    l = []
    for w in s.split():
        if w in l:
            pass
        else:
            l.append(w)
    return " ".join(l)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))