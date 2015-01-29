def getGuessedWord(secretWord, lettersGuessed):
    length = len(secretWord)
    returnList = range(length)

    secretWordList = []
    for c in secretWord:
        secretWordList.append(c)
    
    for i in range(length):
        returnList[i] = "_"
    
    for i in range(length):
        for j in range(len(lettersGuessed)):
            if (lettersGuessed[j] in secretWordList[i]):
                returnList[i] = lettersGuessed[j]
    
    
    
        
    
    makeString = ""
    return makeString.join(returnList)
    
   
    
 
    
    
print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])