num1 = int(input("Insert your first number: "))
num2 = int(input("Insert your second number: "))
operation = input("Insert the operation: ")

if(operation == "*"):
    result = num1 * num2
    print("result = " + str(result))

elif(operation == "+"):
    result = num1 + num2
    print("result = " + str(result))

elif(operation == "-"):
    result = num1 - num2
    print("result = " + str(result))

else:
    print("We don’t support this operation")

