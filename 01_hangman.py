import random
from words import words
import string
from hangman_visual import lives_visual_dict



def get_valid_words(words):
    word = random.choice(words) #randomly chooses something from the list of words
    while "-" in word or " " in word: 
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what letters are already used

    lives = 6

    #getting user_input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(["a", "b", "cd"]) -> "a b cd"
        print("You have", lives ,"remaining and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            
            else: 
                lives = lives - 1 # takes away a life if wrong
                print("Letter is not in word!")

        elif user_letter in used_letters:
            print("You already used that character. Try again")
        
        else:
            print("Invalid char. Please try again!")

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died, sorry the word is: ", word)
    else:
        print("You guessed the word", word)
    

if __name__ == '__main__':
    hangman()




