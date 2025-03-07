import random


hangman = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    '''
]

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = len(hangman) - 1
        self.display_word = ["_" for _ in word]
    
    def display_game_state(self):
        print(hangman[self.incorrect_guesses])
        print("Current word: ", " ".join(self.display_word))
        print(f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
        print("Guessed letters: ", ", ".join(self.guessed_letters))
    
    def make_guess(self, guess):
        guess = guess.lower()
        if guess in self.guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            return False
        if guess not in self.word:
            self.incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        else:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display_word[i] = guess
            print(f"Correct guess! '{guess}' is in the word.")
        self.guessed_letters.append(guess)
        return True

    def word_complete(self):
        return "_" not in self.display_word

    def game_over(self):
        return self.incorrect_guesses >= self.max_incorrect_guesses or self.word_complete()

def main():
    word_list = ["python", "java", "hangman", "programming", "developer", "computer"]
    word_guess = random.choice(word_list)
    game = Hangman(word_guess)
    
    print("Welcome to Hangman!")
    
    while not game.game_over():
        game.display_game_state()
        guess = input("Guess a letter: ")
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a valid letter.")
            continue
        
        game.make_guess(guess) 
    
    if game. word_complete():
        print("Congratulations! You've guessed the word:", game.word)
    else:
        print("Game Over! The word was:", game.word)

if __name__ == "__main__":
    main()