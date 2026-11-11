# Write a program with these functions:
# 1. add(a, b) — returns the sum.
# 2. subtract(a, b) — returns the difference.
# 3. multiply(a, b) — returns the product.
# 4. divide(a, b) — returns the division result and handles division by zero.
# Then:
# - Take two numbers from the user.
# - Call all four functions.
# - Print their returned results.
# Rules:
# - Use return, not print() inside the calculation functions.
# - Use meaningful function names.
# - Handle division by zero properly.

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b == 0):
      return ("Division by zero is not allowed.")
    return a / b

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

print(add(n1,n2))
print(sub(n1,n2))
print(multiply(n1,n2))
print(divide(n1,n2))

# Write two functions:

# Function 1: calculate_sum(*args)
# - Accept any number of integers.
# - Calculate and return their sum.
# Function 2: display_info(**kwargs)
# - Accept any number of keyword arguments.
# - Print each key and its corresponding value.


def calculate_sum(*args):
   sum = 0
   for i in args:
       sum += i

   return sum

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(key, value)


print(calculate_sum(4,5,3,2))
display_info(name="Azra", age=21, cgpa=3.7)


# Write two functions:

# Part A — Scope
# 1. Create a global variable count = 10.
# 2. Create a function update_count().
# 3. Use global to change count to 50.
# 4. Print the value before and after calling the function.
# Part B — Recursion

# Create a recursive function factorial(n) that calculates the factorial of a number.

count = 10

def update_count():
    global count
    count = 50

print("before: ", count)
update_count()
print("after: ", count)

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(7))


# Perform these operations:
# 1. Use map() to calculate the square of every number.
# 2. Use filter() to select numbers divisible by 5.
# 3. Use reduce() to calculate the product of all numbers.
# 4. Use a lambda function wherever appropriate.

nums = [2, 5, 8, 10, 15, 20, 25, 30]
print(list(map(lambda x: x**2, nums)))

print(list(filter(lambda num: num % 5 == 0, nums)))

from functools import reduce
print(reduce(lambda a, b: a * b, nums))


# Write a program that:
# 1. Defines calculate_average(*args) to calculate and return the average of any number of marks.
# 2. Defines student_info(**kwargs) to display student information.
# 3. Defines a lambda function to check whether a number is even.
# 4. Uses map() to double all numbers in a list.
# 5. Uses filter() to select numbers greater than 10.
# 6. Uses recursion to calculate the sum of numbers from 1 to n.

def calculate_average(*args):
    sum = 0
    for i in args:
        sum += i

    return (sum / len(args))

print(calculate_average(2,3,4,5,6))

def student_info(**kwargs):
    for key,val in kwargs.items():
        print(key, val)

student_info(name = "azra", age=21, cgpa=3.7)

even  = lambda a : a % 2 == 0 

print(even(3))
print(even(4))

nums = [3,4,5,6,2]
squares = list(map(lambda a: a **2 , nums))
fil = list(filter(lambda a: a > 10 , nums))

print(squares)
print(fil)

def add(n):
    if(n == 1):
        return 1

    return n + add(n-1)

print(add(5))