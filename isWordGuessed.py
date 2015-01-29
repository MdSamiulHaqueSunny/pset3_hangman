def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag = 1
    # FILL IN YOUR CODE HERE...
    lst = []
    for c in secretWord:
        lst.append(c)
    for i in range(len(secretWord)):
        if (not lst[i] in lettersGuessed):
            flag = 0
            break
    
    if (flag == 1):
        return True
    else:
        return False
            
    



print isWordGuessed('grapefruit', ['z', 'x', 'q', 'g', 'r', 'a', 'p', 'e', 'f', 'r', 'u', 'i', 't'])