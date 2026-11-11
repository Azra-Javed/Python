# Write a program that:
# 1. Takes 5 integers from the user and stores them in a list.
# 2. Prints the original list.
# 3. Prints the largest and smallest elements.
# 4. Sorts the list in ascending order.
# 5. Reverses the list.
# 6. Removes one element entered by the user.
# 7. Prints the final list.

nums = []

for i in range(1,6):
    nums.append(int(input()))

print(nums)

mi = nums[0]
ma = nums[0]

for el in nums:
  
  if(el < mi):
     mi = el
  else:
     ma = el
print("min: ", mi)
print("max: ", ma)

nums.sort()
print(nums)

nums.reverse()
print(nums)

n1 = int(input())
nums.remove(n1)

print(nums)

# Write a program that:
# 1. Creates a tuple containing five integers.
# 2. Prints the first and last elements.
# 3. Prints the tuple in reverse using slicing.
# 4. Counts how many times a user-entered number appears using count().
# 5. Finds the index of a user-entered number using index().
# 6. Unpacks the first three elements into three variables.

t = (4,5,6,4,3)

print(t[0])
print(t[4])

print(t[:: -1])

n = int(input())
print("count: ", t.count(n))

num = int(input())
print(t.index(num))

var1, var2, var3 = t[: 3]
print(var1, var2, var3)

set1 = set()
set2 = set()


length = int(input())

for i in range(1, length+1):
    set1.add(int(input()))
    

for i in range(1, length+1):
    set2.add(int(input()))

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

set1.add(0)
print(set1)
set2.discard(2)
print(set2)


# Create a student management program that:
# 1. Creates a dictionary containing student name, age, and CGPA.
# 2. Prints all keys using keys().
# 3. Prints all values using values().
# 4. Prints all key-value pairs using items().
# 5. Adds a new key called "city".
# 6. Updates the student's CGPA.
# 7. Uses get() to retrieve a key that may not exist.
# 8. Removes the age using pop().


student = {
    "name":"Azra",
    "age":21,
    "CGPA":3.67
}

print(student.keys())
print(student.values())
print(student.items())

student["city"]= "Chunian"
student["CGPA"] = 3.75
student.get("Father", "Not found")
student.pop("age")

print(student.items())


# Write a program that:
# 1. Creates a list of numbers from 1 to 20 using range().
# 2. Creates a new list containing only even numbers using list comprehension.
# 3. Creates another list containing the squares of all numbers using list comprehension.
# 4. Converts the original list into a tuple.
# 5. Converts the original list into a set.
# 6. Creates a dictionary where numbers are keys and their squares are values.

l = []
for i in range(1, 21):
    l.append(i)

even = [i for i in l if i % 2 == 0]
print(even)

squares = [i **2 for i in l]
print(squares)


t = tuple(l)
print(t)

s = set(l)
print(s)

# dic  = {}
# for i in l:
#     dic[i] =  i**2

dic = {i: i**2 for i in l}

print(dic.items())

