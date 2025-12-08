# Task 4: Closure Practice
#Declare a function called make_hangman() that has one argument called secret_word. It should also declare an empty
#  array called guesses. Within the function declare a function called hangman_closure() that takes one argument, 
# which should be a letter. Within the inner function, each time it is called, the letter should be appended to the
#  guesses array. Then the word should be printed out, with underscores substituted for the letters that haven't been
#  guessed. So, if secret_word is "alphabet", and guesses is ["a", "h"], then "a__ha__" should be printed out. 
# The function should return True if all the letters have been guessed, and False otherwise. make_hangman() should 
# return hangman_closure.
def make_hangman(secret_word):
    guesses =[]
    
    def hangman_closure(letter):
        guessed_word= ""
        
        if letter not in guesses:
            guesses.append(letter)

        for char in secret_word:
            if char in guesses:
                guessed_word += char
            else:
                guessed_word += "_"
        print(guessed_word)
        return guessed_word == secret_word
    return hangman_closure
# 3. Within hangman-closure.py, implement a hangman game that uses make_hangman(). Use the input() function to prompt
#  for the secret word. Then use the input() function to prompt for each of the guesses, until the full word is guessed.      
secret_word = input("enter a secret word: ")
hangman_game = make_hangman(secret_word)
while True:

    guessed_letter = input("enter a guessed letter: ")
    game_over = hangman_game(guessed_letter)
    if game_over:
        break
    
