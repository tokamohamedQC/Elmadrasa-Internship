import random

def guessing_game():
    # Initialize high score to a large number
    high_score = float('inf')

    while True:
        # Generate a random number between 1 and 10
        secret_number = random.randint(1, 10)

        attempts = 0

        while True:
            # Get user input for a guess
            user_guess = int(input("Guess the number (between 1 and 10): "))
            
            # Increment the attempts counter
            attempts += 1

            # Check if the guess is correct
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

                # Update the high score if the current attempts are less than the existing high score
                high_score = min(high_score, attempts)
                
                print(f"Current high score: {high_score}")
                
                break
            else:
                print("Wrong guess. Try again!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
guessing_game()