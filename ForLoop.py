#for loop in python:
#     For Loops are used for iterating over a sequence like lists, tuples, strings, and ranges.

# For loop allows you to apply the same operation to every item within loop.
# Using For Loop avoid the need of manually managing the index.
# For loop can iterate over any iterable object, such as dictionary, list or any custom iterators.
# For Loop Example:

s = ["Akash", "Rohan", "Sohan"]

# using for loop with string
for i in s: # i is a control variable or iteration variable.
    print(i)

#Python For Loop with String

n = "Akash"
for name  in n: # we can take any name for iteration variable/ control variable.
    print(name)

    #Using range() with For Loop

    # range() function is used to generate a sequence of numbers.
    # It is used to iterate over a sequence of numbers.
    # range() function can take 1, 2 or 3 arguments.
    # range(stop) - generates a sequence from 0 to stop-1.
    # range(start, stop) - generates a sequence from start to stop-1.
    # range(start, stop, step) - generates a sequence from start to stop-1 with a step size.

for i in range(0, 10, 2):
    print(i)

    #Control Statements with For Loop
    #Loop control statements alter the normal execution flow within loops.
    #  When the execution exits the loop's scope, any objects created in the scope are automatically destroyed.
    # 1. Break Statement:
    # Terminates the loop and transfers control to the statement immediately following the loop.

    for i in 'Akash':

    # break the loop as soon it sees 'e'
    # or 's'
     if i == 'a' or i == 's':
        break

print(i)

# 2. Continue Statement:
# Skips the current iteration and continues with the next iteration of the loop.

# Prints all letters except 'e' and 's'

for i in 'Akash':

    if i == 'a' or i == 's':
        continue
    print(i)

# 3. Pass Statement:

# An empty loop
for i in 'Akash':
    pass
print(i)

# Else Statement with For Loops

# Python allows an else block to be used with for or while loops. The else block is executed only if the loop completes normally (i.e., not terminated by a break statement).

# Example:

for i in range(1, 8):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

# Using Enumerate with for loop
        
# The enumerate() function in Python is used with a for loop to iterate over an iterable
# (like a list, tuple, or string) while keeping track of the index of each item.

li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print (i, j)

    #Nested For Loops in Python
    #Nested for loops are loops within loops, where the inner loop is executed completely for each iteration of the outer loop. 
    # This is commonly used to iterate over combinations of elements from multiple ranges or collections.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


        #----------------------------------------Question/Answer------------------------------------------------

#         Python For Loop Exercise Questions
# Below are two Exercise Questions on Python for-loops. We have covered continue statement and range() function in these exercise questions.

# Q1. Code to implement Continue statement in for-loop



# 1
# a = ["shirt", "sock", "pants", "sock", "towel"]
# 2
# b = []
# 3
# for i in a:
# 4
#     if i == "sock":
# 5
#         continue
# 6
#     else:
# 7
#         print(f"Washing {i}")
# 8
# b.append("socks")
# 9
# print(f"Washing {b}")

# Output
# Washing shirt
# Washing pants
# Washing towel
# Washing ['socks']
# Q2. Code to implement range function in for-loop



# 1
# for i in range(1, 8):
# 2
#     d = 3 + (i - 1) * 0.5
# 3
#     print(f"Day {i}: Run {d:.1f} miles")

# Output
# Day 1: Run 3.0 miles
# Day 2: Run 3.5 miles
# Day 3: Run 4.0 miles
# Day 4: Run 4.5 miles
# Day 5: Run 5.0 miles
# Day 6: Run 5.5 miles
# Day 7: Run 6.0 miles


# Test Your Knowledge – Python For Loop Quiz



# Python For Loops – FAQs
# What is syntax of for loop in Python?
# The syntax of a for loop in Python is straightforward. It iterates over a sequence (like a list, tuple, string, etc.) and executes the block of code inside the loop for each element in the sequence.


# for item in sequence:
#     # Code block to execute
# How to iterate with an index in a for loop in Python?
# You can use the ‘enumerate()’ function to iterate over a sequence and retrieve both the index and the value of each element.


# for index, item in enumerate(sequence):
#     # Use index and item inside the loop
# Can you provide examples of for loops in Python?
# Sure! Here are some examples of for loops in Python:


# # Example 1: Iterating over a list
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)

# # Example 2: Iterating over a string
# for char in 'Python':
#     print(char)

# # Example 3: Using enumerate to get index and value
# for index, num in enumerate([10, 20, 30]):
#     print(f'Index {index}: {num}')

# # Example 4: Iterating over a dictionary
# person = {'name': 'John', 'age': 30}
# for key, value in person.items():
#     print(f'{key}: {value}')
# How to write a for loop in Python?
# To write a for loop, specify the variable that will hold each item from the sequence (‘item’ in the examples above), followed by the keyword in and the sequence itself (‘sequence’ in the examples).


# # Basic syntax
# for item in sequence:
#     # Code block to execute
# How to use for loops in Python?
# For loops are used to iterate over sequences (like lists, tuples, strings, dictionaries) and perform operations on each element or key-value pair. They are fundamental for iterating and processing data in Python.


# # Example: Calculating sum of numbers in a list
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(f'Total sum: {total}')

        





