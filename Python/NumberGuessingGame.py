import random


def numberGuessingGame():
    computer_guess = random.randint(1, 100)
    total_Guess = 5;

    attempts = 0

    while attempts != total_Guess:
        user_guess = input("Enter your guess: ")
        user_guess = int(user_guess)

        if user_guess == computer_guess:
            print("Correct!")
            break
        elif user_guess > computer_guess:
            print("Too High")
            attempts += 1
            print(f"Total attempts {attempts }/5")
        else:
            print("Too Low")
            attempts += 1
            print(f"Total attempts {attempts }/5")
            
    print(f"Game Over! The number was {computer_guess}")

numberGuessingGame()
