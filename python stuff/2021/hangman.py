import random
from words import words
import string
def get_valid_word(words):
    word=random.choice(words)#randomly chooses something from the list
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word
def hangman():
    word = get_valid_word(words)
    word_letters=set(word)#letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set()#what the user has guessed

    lives=6

    # getting user input
    while len(word_letters)>0 and lives>0:
        #letters used
        # '-.join(['a', 'b', 'cd'])-->'a b cd'
        print('you have', lives, 'lives left and you used these letters ', ' '-join(used_letters))



               #what current word (ie w->r d)
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('current word ', ' '.join(word_list))
        user_letter=input('Guess a letter ').upper()
        if user_letter in alphabet - used_letters:
         used_letters.add(user_letter)
         if user_letter in word_letters:
            word_letters.remove(user_letter)

         else:
            lives=lives-1 # takes away a life if wrong
            print('letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again')
        else:
            print('Invalid character. Please try again')
    if lives==0:
        print('You died, sorry, the word was', word)
    else:
        print('You guessed the word', word)




