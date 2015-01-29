# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "H:\pset3_hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    if (lettersGuessed in availableAlphabetList):
        availableAlphabetList.remove(lettersGuessed)
        return True
    else:
        return False
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

availableAlphabetList = []
for c in string.ascii_lowercase:
    availableAlphabetList.append(c)



def matchLetters(stringArray, letter):
    k = 0
    while (k < secretWordLength):
        if (letter in secretWord[k]):
            guessStringList[k] = letter
            m[k] =  True
        else:
            m[k] = False
        k += 1
    if True in m:
        return True
    else:
        return False
    

print "Welcome to the game Hangman!"
secretWord = random.choice(wordlist)
secretWordLength = len(secretWord)
guessStringList = range(secretWordLength)
m = range(secretWordLength)
i = 0
while (i < secretWordLength):
    if (i % 2 == 0):
        guessStringList[i] = '_'
    else:
        guessStringList[i] = ' '
    i += 1

hello = ""
hello.join(guessStringList)

print "I am thinking of a word that is " + str(secretWordLength) + " letters long " + secretWord
chance = 8
booleanChance = 0
lastFlag = 0

secretWordList = []

for c in secretWord:
    secretWordList.append(c)

while (chance > 0):
    availableAlphabetString = ""
    print availableAlphabetString.join(availableAlphabetList)
    guessedLetter = raw_input("Insert a letter ")
    repeat =  getAvailableLetters(guessedLetter)
    while(repeat == False):
        guessedLetter = raw_input("Oops! You've already guessed that letter: ")
        repeat = getAvailableLetters(guessedLetter)
    booleanChance = matchLetters(secretWord, guessedLetter)
    print "Boolean chance: " , booleanChance
    if(booleanChance == False):
        chance -= 1
        print "Letter not found, you have " , chance , " left"
        hello = ""
        print hello.join(guessStringList)
        print "secretwordlist ", secretWordList
        print "Guessstringlist ", guessStringList
    else:
        hello = ""
        print hello.join(guessStringList)
        print "secretwordlist ", secretWordList
        print "Guessstringlist ", guessStringList
    if (secretWordList == guessStringList):
        lastFlag = 1
        break


if (lastFlag == 1):
    print "You guessed the word"
else:
    print "You couldn't guess it, the word was ", secretWord


    
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
