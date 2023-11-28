import random

user = input("please enter your choice in Game?\n")
PC = random.choice(['p','r','s'])

print("User played: " + user)
print("PC played: "+ PC)
if (user == PC):
    print("It's a tie")
elif((user == 'p' and PC == 'r') or (user == 'r' and PC == 's') or (user == 's' and PC == 'p')):
    print("user win")
else:
    print("PC win")