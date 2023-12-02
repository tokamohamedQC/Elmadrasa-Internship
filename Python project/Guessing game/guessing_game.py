import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("Ther's no score, start playing")
    else:
        print(f"The current high score is {min(attempts_list)}")

attempts = 0
rand_list = random.randint(1,10)

print("Welcome to guessing game")

player_name = input("What is your name?\n")
wanna_play = input(
    f"Want to play the guessing game, {player_name}?\n"
    "Enter yes/no: "
    ).lower()

if wanna_play == "no":
    print("That's cool")
    exit()
else:
    show_score()

while wanna_play == "yes":
    try: 
        guess = int(input("Guess a number between 1 and 10?\n"))
        if (guess < 1 or guess > 10):
            raise ValueError("Please enter a number within range")
        
        attempts += 1
        attempts_list.append(attempts)
        
        if(guess == rand_list):
            print("That's correct")
            print(f"It took you {attempts} attempts to get it right")
            wanna_play = input("wanna play again? Enter yes/no: ").lower()
            if wanna_play == "no":
                print("That's cool, see you!")
            else:    
                attempts = 0
                rand_list = random.randint(1,10)
                show_score()
                continue
        elif(guess > rand_list):
            print("It's lower")
        else:
            print("It's higher")
    except ValueError as err:
        print(err)
    