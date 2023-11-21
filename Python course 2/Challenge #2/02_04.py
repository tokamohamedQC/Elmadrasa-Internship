fruits = [
    "Apple",
    "Bananas",
    "Grapes",
    "Mangoes",
    "Nectarines",
    "Pears"
]

print("This is Challeng 2")

for fruit in fruits:
    print(fruit)

#Solution 1
counter1 = 0
while (counter1 != 4):
    print(fruits[counter1])
    counter1 += 1

counter = 0
#Solution 2
while (fruits[counter] != "Nectarines"):
        print(fruits[counter])
        counter += 1
