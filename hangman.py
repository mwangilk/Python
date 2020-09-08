def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for letter in secretWord :
      if letter not in lettersGuessed :
        return False
        
    return True
####
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word =''
    for letter in secretWord :
       if letter in lettersGuessed:
          word += letter
       else :
           word += '_ '
    return word
###
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    letters = string.ascii_lowercase
    word = ''
    for i in letters :
     if i not in lettersGuessed:
        word += i
    return word
      
#####
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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +" letters long")
    print("-----------")
    lettersGuessed = []
    Guesses = 8
    while not isWordGuessed(secretWord, lettersGuessed) and Guesses > 0:
        print("You have " + str(Guesses) +" guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        while True:
            Letter = raw_input("Please guess a letter: ")
            Guess = Letter.lower()
            if Guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                print("	You have " + str(Guesses) +" guesses left")
                print("Available Letters: " + getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += Guess
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("Congratulations, you won!")
            break
        elif Guess in secretWord:
             print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
             print("-----------")
       
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            Guesses -= 1
        
        if Guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

