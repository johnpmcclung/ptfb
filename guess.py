"""
guessing game

"""

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
    else:
        print(f"Try again... (Attempt {guess_count} / {guess_limit})")
    
else:
    print("Limit of 3 guesses reached. Goodbye!")

