def getAvailableLetters(lettersGuessed):
    import string
    lst = []
    for c in string.ascii_lowercase:
        lst.append(c)
    i = 0
    while (i < len(lettersGuessed)):
        if (lettersGuessed[i] in lst):
            lst.remove(lettersGuessed[i])
    
        i += 1
    
    makeString = ""
    return makeString.join(lst)


print getAvailableLetters(['a'])