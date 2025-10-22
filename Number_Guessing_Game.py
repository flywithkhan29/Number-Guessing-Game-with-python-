import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

attempts = 0
while True:
    guess = int(input("Enter your guess:"))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You have guessed the number {secret_number}")
        break

play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again == "yes":
    secret_number = random.randint(1, 100)
    attempts = 0
    print("New game started! Guess a number between 1 and 100.")
    while True:
        guess = int(input("Enter your guess:"))
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You have guessed the number {secret_number}")
            break
else:
    print("Thank you for playing! Goodbye.")
