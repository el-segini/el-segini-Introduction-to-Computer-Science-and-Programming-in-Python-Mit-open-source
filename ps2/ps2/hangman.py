# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    num = sum(map(lambda x:x in letters_guessed,secret_word))
    if num == len(secret_word):
        return True
    else:
        return False
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_list = list(map(lambda x:"_ " if x != " " else " " ,secret_word))
    
    for idx,char in enumerate(secret_word):
        if char in letters_guessed:
                word_list[idx] = char
                
    show_word = "".join(word_list)        
    return show_word
    
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    not_guessed = "".join(list(filter(lambda x: x not in letters_guessed ,letters)))
    
    return not_guessed
 
   

def msgs(guesses,warnings,guessed_letters,secret_word):
    '''

    guesses : int,number of left attempts.
    warnings : int,number of left warnings
    guessed_letters : list, the strings that the user have guessed
    secret_word : string ,the word the user is guessing; assumes all letters are lowercase

    Returns: none
    -------
    it prints the specific msgs that i want about to show to th player

    '''
    if guesses > 0:
        print('you have {} attempts'.format(guesses))
        print('you have {} warnings'.format(warnings))
        print('your available letters is : ',get_available_letters(guessed_letters))
        print(get_guessed_word(secret_word, guessed_letters))
    else:
        print("you have used all of your attempts")
        print('you have lost, the secret word is', secret_word)
    
    
    
def attempt_penality(letter):
    """
    letter : string, the guessed letter by the user
    Returns: int , the value of the penality of the letter
    """
    vowels = ['a','e','i','o']
    if letter in vowels:
        return 2
    else:
        return 1
    
def warnings_counter(warnings):
    if warnings > 0:
       warnings -= 1
       return warnings
    else:
       warnings = 0
       return warnings 

def guesses_warnings_counter(guesses,warnings):
    if warnings == 0:
        guesses -= 1
        return guesses
    else:
        return guesses
   
             
def unique_letters(secret_word):
    '''
    secret_word : string, the word the user is guessing
    return : number of unique letters in the word
    '''
    unique_letters = []
    for i in secret_word:
        if i not in unique_letters:
            unique_letters.append(i)
    return len(unique_letters)

def welcome(secret_word):
    print("welcome to the game hangman! \ni'm thinking of a word that is {} letters long. ".format(len(secret_word)))
    print("--------------------------------------")
    
def hangman(secret_word='iillovveyouu'):
   
    guesses = 6
    warnings = 3
    guessed_letters = []
    welcome(secret_word)

    msgs(guesses,warnings,guessed_letters,secret_word)
        
    while guesses > 0 :
        
        guess_letter = input('enter your letter: ').lower()
        
        #checking if me word is guessed
        my_word_guessed = is_word_guessed(secret_word, guessed_letters)
        if my_word_guessed : 
            print('congratulations you have won the game')
            print(guesses * unique_letters(secret_word))      
            break
        
        if (guess_letter not in string.ascii_lowercase):
            print('please enter a valid alphabet')
            warnings = warnings_counter(warnings)
            guesses = guesses_warnings_counter(guesses,warnings)
            msgs(guesses,warnings,guessed_letters,secret_word)
                      
        elif guess_letter in guessed_letters:
            print("Oops! You've already guessed that letter.\n")
                
            warnings = warnings_counter(warnings)
            guesses = guesses_warnings_counter(guesses,warnings)
                
            msgs(guesses,warnings,guessed_letters,secret_word)
                
        elif (guess_letter not in secret_word) and (guess_letter not in guessed_letters):
            print('wrong guesss :',guess_letter,'\n')
            guessed_letters.append(guess_letter)
            guesses -= attempt_penality(guess_letter)
            msgs(guesses,warnings,guessed_letters,secret_word)
        else:
            print('good guess: ', guess_letter,'\n')
            guessed_letters.append(guess_letter)
            msgs(guesses,warnings,guessed_letters,secret_word)

    
   

    

    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #removing whitespaces from my word
    my_word_no_gaps = my_word.replace(' ','')
    
    count = 0
    
    #checking on the actual letters of my guesses
    if len(my_word_no_gaps) == len(other_word):
        for idx,char in enumerate(my_word_no_gaps) :
            if char in string.ascii_letters and char == other_word[idx]:
                count += 1
    else:
        return False         
    
    
    return True if count == len(my_word_no_gaps.replace('_', '')) else False     
            


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    match = ""
    if len(my_word.replace("_ ", "")) > 1: 
        for word in wordlist:
            if match_with_gaps(my_word,word):
                match += word + " "
                match.rstrip()
    else:
        match = "you need to guess 2 right letters at least"
        
    return match
 
    
def letter_checker(letter):
    return True if letter in string.ascii_lowercase else letter

def unique_guess(letter,letters_guessed):
    if letter in letters_guessed:
        return letters_guessed 
    else:
        return letters_guessed.append(letter)
    
        
        

def hangman_with_hints(secret_word):
  
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    attempts = 6
    welcome(secret_word)
    letters_guessed = []
    print(get_guessed_word(secret_word, letters_guessed))
    while attempts > 0:
        
        print('\nyou have {} attempts left'.format(attempts))
        
        letter_guess = input('please guess a letter: ').lower()
        
        valid_letter = letter_checker(letter_guess)
         
        # print('secret_word is:',secret_word)
        
        if valid_letter == True :
            letters_guessed.append(letter_guess)
            if letter_guess in secret_word :
                print('good guess: ',get_guessed_word(secret_word, letters_guessed))
            else:
                print(get_guessed_word(secret_word, letters_guessed))
                attempts -= attempt_penality(letter_guess)
            

        elif valid_letter == "*" :
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            
        else:
            print('please enter valid alphabet or * for hint')
            
            
        is_my_word_guessed = is_word_guessed(secret_word,letters_guessed)
        if is_my_word_guessed:
            print('congratulations you have won the game')
            print('your score is:',attempts * unique_letters(secret_word))      
            break
   
    if attempts <= 0:
        print('you have lost the game and the secret word is',secret_word)
        
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
# #     # pass

# #     # To test part 2, comment out the pass line above and
# #     # uncomment the following two lines.
    
# #     secret_word = choose_word(wordlist)
# #     hangman(secret_word)

# ###############
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
