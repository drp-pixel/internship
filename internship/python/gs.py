# Guess the Number Game (while loop)

# Store the secret number that the user needs to guess
secret = 7

print("Welcome to Guess the Number Game!")

# Initialize guess variable with None (so the loop starts)
guess = None

# Keep looping until the user guesses the correct number
while guess != secret:
    # Ask the user to input a number
    guess = int(input("Guess the number:"))
    
    # Check if the guess is correct
    if guess == secret:
        print("Correct! ")   # Success message
    else:
        print("Try again...") # Hint to keep guessing

# Guess the Number Game (with for loop)

secret = 7

print("Welcome to Guess the Number Game!")

# Infinite for loop using iter()
for _ in iter(int, 1):   # runs forever until break
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! You guessed the number!")
        break
    else:
        print("Try again...")