
#while Loop is used to execute a block of code multiple times until a given condition is satisfied. when the condition becomes false , the line immediately after the loop in the program is executed .


#exaple of while loop
count = 0
while (count <3):
    count = count +1
    print("Hello world")

    #while loop syntax
    # while expression:
    #     statement(S)

    #infinite while Loop

    #value of the condition is always True. 
    # Therefore, the body of the loop is run infinite times until the memory is full.
#     age = 25
# # test conditon is alwas true/false
#     while age > 18:
#         print('print you are and audlt')

#         while loop with continue statement. 
# it returns the control to the beginning of the loop.

# Example:
# print all letters except 'e' and 's'

i = 0
a = 'Akash'

while i < len(a):
    if a[i] == 'k' or a[i] == 's':
        i = i + 1
        continue   
    print('current letter:', a[i])
    i = i + 1

    #example-2

    x = 0
y = 'mango'

while x < len(y):
    if y[x] == 'm' or y[x] == 'a':
        x = x + 1
        continue  # Skip to the next iteration for 'm' or 'a'
    print('own letter:', y[x])
    x = x + 1

    #while loop with break statement--->it brings control out of the loop.

    #Example:

i = 0
a = 'laptop'

while i < len(a):
    if a[i] == 'p' or a[i] == 't':  # Check if the character is 'p' or 't'
        break  # Exit the loop when 'p' or 't' is encountered
    print('remaining letter:', a[i])  # Print the current character
    i += 1  # Increment the index

    #while loop with pass statement

    # An empty loop
a = 'Akash'
i = 0

while i < len(a):
    i += 1
    pass
  
print('Value of i :', i)

#while loop with else statement
# Python program to demonstrate
# while-else loop

i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")


#----------------------------------------Question/Answer------------------------------------------------

# While Loops in Python
# Syntax of a While Loop:


# while condition:
#     # code block to execute
# The loop runs as long as the condition evaluates to True.
# Typical Use Cases:

# Repeating tasks until a condition is met (e.g., reading lines from a file).
# Continuously prompting the user for valid input.
# Running the main loop of a game until the player exits.
# Polling or checking the status of a resource.
# Controlling While Loops:

# break: Exits the loop immediately.
# Example:

# while True:
#     s = input("Enter something (or 'quit' to stop): ")
#     if s == 'quit':
#         break
#     print(f"You entered: {s}")
# continue: Skips the rest of the code in the current iteration and starts the next iteration.
# Example:

# cnt = 0
# while cnt < 10:
#     cnt += 1
#     if cnt % 2 == 0:
#         continue
#     print(cnt)  # Prints only odd numbers
# Dangers of While Loops:

# Infinite Loops: If the condition never becomes false, the loop runs forever. Example:

# while True:
#     print("This will run forever!")
# Resource Exhaustion: Continuous loops can consume CPU and memory, leading to performance issues.
# Complexity: Complex or nested loops may reduce readability and maintainability.
# Using While Loops for User Input:

# Example:

# s = ""
# while s.lower() != "exit":
#     s = input("Enter something (type 'exit' to stop): ")
#     if s.lower() != "exit":
#         print(f"You entered: {s}")
# print("Goodbye!")
# This loop repeatedly asks for input until the user types "exit".












       