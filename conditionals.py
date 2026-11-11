# Write a program that takes a number from the user and checks whether it is:
# - Positive
# - Negative
# - Zero


num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Write a program that:
# 1. Prints numbers from 1 to 20 using for and range().
# 2. Skips multiples of 3 using continue.
# 3. Stops when the number reaches 17 using break.
# 4. Uses pass in an if condition when the number is 10.


for i in range(1, 21):
    if (i % 3 == 0):
        continue

    if(i == 10):
        pass

    if(i == 17):
        break

    print(i)


# Write a program that:
# 1. Takes a number from the user.
# 2. Uses a while loop to print its multiplication table from 1 to 10.
# 3. Also calculate the sum of numbers from 1 to that number using a while loop.


num = int(input("Enter num: "))

i = 1
while(i <= 10):
    print(num ,"*", i, " = ", num * i)
    i += 1

i = 1
total = 0

while(i <= num):
    total += i
    i += 1

print("sum: ", total)


# program to print stars

rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Write a simple calculator that:
# 1. Takes two numbers from the user.
# 2. Takes an operator (+, -, *, /).
# 3. Uses match-case to perform the operation.
# 4. Handles division by zero.
# 5. Prints an invalid-operator message for unsupported operators.

num1 = int(input("num1: "))
num2 = int(input("num2: "))

op = input("Enter op: ")

match op:
    case "+": 
        print (num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if(num2 == 0):
            print("disivion by 0 is not allowed")
        else:
            print(num1 / num2)
    case _:
        print("invalid operator")

