# This program prints student's name, age, cgpa and Enrollent status

Name = "Azra"
Age = 21
CGPA = 3.67
isEnrolled = True

print("Name:",Name)
print("Age: ",Age)
print("CGPA: ",CGPA)
print("Enrolled: ",isEnrolled)

print("Data types:")
print(type(Name))
print(type(Age))
print(type(CGPA))
print(type(isEnrolled))

# 2. Operators

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("Sum: ", num1 + num2)
print("Difference: ", num1 - num2)
print("Product: ", num1 * num2)
print("Division: ", num1 / num2)
print("Floor Division: ", (num1 // num2))
print("Modulus: ", num1 % num2)
print("Power", num1 ** num2)


# Write a Python program that:
# 1. Takes a student's name as a string.
# 2. Takes three subject marks using input().
# 3. Converts the marks into integers.
# 4. Calculates total marks.
# 5. Calculates percentage assuming each subject is out of 100.
# 6. Converts the percentage into an integer and displays it.
# 7. Displays the data type of the original percentage and converted percentage.

name = input("Enter your name: ")
phy = int(input("physics: "))
chem = int(input("chemistry: "))
math = int(input("math: "))

total_marks = phy + chem + math
percentage = (total_marks / 300) * 100
int_percentage = int(percentage)
print("Percentage: ", percentage)

print(type(percentage))
print(type(int_percentage))


# Write a program that:
# 1. Takes two integers from the user.
# 2. Checks and prints:
#    - Is the first number greater than the second?
#    - Are both numbers equal?
#    - Is the first number even?
#    - Is the second number odd?
#    - Are both numbers positive?
#    - Is at least one number divisible by 5?
#    - Are both numbers between 1 and 100 (inclusive)?


n1 = int(input("n1: "))
n2 = int(input("n2: "))

print("First > Second: ", n1 > n2)
print("Both Equal: ", n1 == n2)
print("First is Even: ", n1 % 2 == 0)
print("Second is Odd: ", n2 % 2 != 1)
print("Both positive: ", n1 > 0 and n2 > 0)
print("At least one divisible by 5: ", (n1 % 5 == 0 or n2 % 5 == 0))
print ("Both between 1 and 100: ", (n1 > 0 and n1 <=100) and (n2 > 0 and n2 <= 100) )


# Write a program that:
# 1. Takes an integer num from the user.
# 2. Initially assigns num to a variable called x.
# 3. Performs these operations on x, in order:

# Operation	Assignment
# Add 10	         +=
# Subtract 5	     -=
# Multiply by 2	     *=
# Divide by 3	     /=
# Raise to power 2 	**=

# 4. Print x after every operation.
# 5. Also demonstrate floor division (//=) and modulus (%=) using a separate variable so that all operators can be observed independently.


num = int(input("num: "))
x = num

x += 10
print("x: ", x)
x -= 5
print("x: ", x)
x *= 2
print("x: ", x)
x /= 3
print("x: ", x)
x **= 2
print("x: ", x)

y = num
y //= 2
print("y: ", y)

y = num
y %= 2 
print("y: ", y)

