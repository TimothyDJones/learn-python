# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

#__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#WORDLIST_FILENAME = open(os.path.join(__location__, 'words.txt'))
WORDLIST_FILENAME = "/home/tim/projects/edx_6.00.1x_python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    for c in secretWord:
        if c not in lettersGuessed:
            return False
            
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_word = ""
    for c in secretWord:
        if c in lettersGuessed:
            guessed_word += c
        else:
            guessed_word += "_ "    
    
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    avail_letters = string.ascii_lowercase
    for c in lettersGuessed:
        avail_letters = avail_letters.replace(c, '')
    
    return avail_letters


def is_already_guessed(letter, lettersGuessed): 
    '''
    letter: character, the character
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, indicates whether character is already
      in the list
    '''
    result = False
    if (len(letter) != 1) or letter in lettersGuessed or letter not in string.ascii_lowercase:
      result = True

    return result

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
    guess_remain = 8
    available_letters = string.ascii_lowercase
    guessed_letters = []
    disp_message = ""

    print("Welcome to the game, Hangman!")
    print("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print(12 * "-")

    while True:
      if guess_remain <= 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        break
      print("You have " + str(guess_remain) + " guesses left.")
      print("Available letters: " + available_letters)
      guess = input("Please guess a letter: ").lower()
      if not is_already_guessed(guess, guessed_letters):
        guessed_letters.append(guess)
        if guess not in secretWord:
          guess_remain -= 1
          disp_message = "Oops! That letter is not in my word: "
        else:
          disp_message = "Good guess: "
      else:
        disp_message = "Oops! You've already guessed that letter: "

      available_letters = getAvailableLetters(guessed_letters)
      print(disp_message + getGuessedWord(secretWord, guessed_letters))
      print(12 * "-")

      if isWordGuessed(secretWord, guessed_letters):
        print("Congratulations, you won!")
        break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = "zzz"
hangman(secretWord)
