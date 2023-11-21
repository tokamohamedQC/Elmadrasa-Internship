num1 = int(input("Insert your first number: "))
num2 = int(input("Insert your second number: "))
operation = input("Insert the operation: ")

import math;
import random2;
from modules import calculate;

if(operation == "*"):
    result = calculate.multi(num1,num2)
   
elif(operation == "+"):
    result = calculate.sum(num1,num2)

elif(operation == "-"):
    result = calculate.subtract(num1,num2)

elif(operation == "/"):
    result = calculate.divide(num1,num2)

elif(operation == "Power"):
    result = math.pow(num1,num2)

elif(operation == "Sqrt"):
    result = math.sqrt(num1)

elif(operation == "Random"):
    result = random2.randint(num1,num2)

else:
    print("We don’t support this operation")

print(f"result = {result}")