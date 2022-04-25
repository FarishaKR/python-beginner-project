import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '' in word:
        word = random.choice(words)
    return word
def hangman():
    word = get_valid_word(words)
    word_leters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
       used_letters.add(user_letter)
       if user_letter in word_leters:
           word_leters.remove(user_letter)
           
    elif user_letter in used_letters:
        print('you have already used that character. Please try again. ')
    else:
        print('invalid character.Please try again!')

hangman()
    
