
#break statement

# The break statement is used to exit a loop prematurely, regardless of the loop's condition or remaining iterations.

# Usage:

# Works with both for and while loops.
# Transfers control to the next line of code after the loop.


# Common Use Cases:

# Exit a loop when a specific condition is met.
# Stop unnecessary iterations to save time and resources.

#syntax:

# while condition:
#     if break_condition:
#         break

# Example:1

# Example: Searching for an element in a list

a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")



# Example:2

# Using For Loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    
# Using While Loop
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    i += 1


    #Example:3
    #break statement with for lop

for i in range(10):
    print(i)
    if i == 6:
        break

# break statement with while loop
    
    cnt = 5

while True:
    print(cnt)
    cnt -= 1
    if cnt == 0:
        print("Countdown finished!")
        break  # Exit the loop

    #Example:4

    #using break in nested loop

    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
val = 5
found = False

for r in matrix:
    for n in r:
        if n == val:
            print(f"{val} found!")
            found = True
            break  # Exit the inner loop
    if found:
        break  # Exit the outer loop
