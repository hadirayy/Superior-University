import random
class FizzBuzzGame:
    def __init__(self):
        self.random_number = 0
    def generate_random_number(self):
        self.random_number = random.randint(1,100)
        print(f"Random number:{self.random_number}")
    def fizz_buzz(self):
        if self.random_number % 3 == 0 and self.random_number % 5 == 0:
            return "FizzBuzz"
        elif self.random_number % 3 ==0:
            return "Fizz"
        elif self.random_number % 5 ==0:
            return "Buzz"
        else:
            return "Neither"
    def start_game(self):
        self.generate_random_number()
        user =input("Is the number 'Fizz' , 'Bizz' or 'Neither' ").strip()
        correct_answer=self.fizz_buzz()
        if user.lower() == correct_answer.lower():
            print("Correct Answer")
        else:
            print(f"The correct Answer wa:{correct_answer}")
game=FizzBuzzGame()
game.start_game()

    

