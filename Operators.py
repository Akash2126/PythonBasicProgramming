

# ---------------------------------------------------------------------Airthmetic Operators---------------------------------------------------------------------


# arithmetic operators are symbol that performed a mathematical calculations on numeric values:


# Addition (+): Adds two numbers.
num1=10
num2=20
res=num1+num2
print(res)

# Subtraction (-): Subtracts one number from another.
a=10
b=5
res = a-b
print(res)

# Multiplication (*): Multiplies two numbers.
c= 5
d=6
res = c*d
print(res)

# Division (/): Divides one number by another, returning a float.
e= 10
f = 2
res = e/f
print(res)

# Modulus (%): Returns the remainder of a division operation.
g = 10
h = 3
res = g%h
print(res)

#Exponentiation Operator (**):raises the first operand to the power of the second.

i = 2
j = 3
res = i**j
print(res)

# Floor Division Operator (//): divides two numbers and returns the largest integer less than or equal to the result 
# (i.e., it performs division and rounds down).

k = 10
l= 3
res =k//l 
print(res)

m = -7
n= 3
res =k//l 
print(res)

#-------------------------------------------------------------------------Question----------------------------------------------------------------

# In Python, arithmetic operators follow the BODMAS/BIDMAS rule (order of operations):

# Brackets: Evaluate expressions inside parentheses first.
# Orders: Handle exponentiation (**).
# Division and Multiplication: Process /, *, //, % left to right.
# Addition and Subtraction: Process + and - left to right.
# Example:
result = 3 + 2 * 2 ** 2 / 2 - 1  # Output: 6.0
# Explanation: Exponentiation → Multiplication → Division → Addition → Subtraction

# In Python, there is no === operator.

# ==: Used to check if the values of two objects are equal.
# is: Used to check if two variables refer to the same object in memory (identity comparison).
# Example:
a = 10
b = 10
print(a == b)  # True (values are equal)
print(a is b)  # True (same object in memory for small integers)

# ---------------------------------------------------------------------Comparison Operators---------------------------------------------------------------------    


# comparison operators are used to compare the values of two operands. These operators return a boolean result (True or False). The key comparison operators include:

# Equal to (==): Checks if two operands are equal.
# Not equal to (!=): Checks if two operands are not equal.
# Greater than (>): Checks if the left operand is greater than the right operand.
# Less than (<): Checks if the left operand is less than the right operand.
# Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
# Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.

a = 10
b = 20
print(a == b)   # False
print(a < b)    # True
print("apple" > "banana")  # False
print("apple" < "banana")  # True

# > (Greater than): Returns True if the left operand is greater than the right.
# Example: x > y

# < (Less than): Returns True if the left operand is less than the right.
# Example: x < y

# == (Equal to): Returns True if both operands are equal.
# Example: x == y

# != (Not equal to): Returns True if the operands are not equal.
# Example: x != y

# >= (Greater than or equal to): Returns True if the left operand is greater than or equal to the right.
# Example: x >= y

# <= (Less than or equal to): Returns True if the left operand is less than or equal to the right.
# Example: x <= y


# the Equality Operator (==) is used to check if two operands (values) are equal. It returns True if both operands are equal and False otherwise.

# Example:
a = 9
b = 5
c = 9

# Checking if 'a' is equal to 'b'
print(a == b)  # Output: False

# Checking if 'a' is equal to 'c'
print(a == c)  # Output: True

# The Not Equal Operator (!=) is used to check if two operands are not equal. It returns True if the operands are different and False if they are equal.

a = 9
b = 5
c = 9

# Checking if 'a' is not equal to 'b'
print(a != b)  # Output: True

# Checking if 'a' is not equal to 'c'
print(a != c)  # Output: False

# Greater Than Operator (>) is used to check if the left operand is greater than the right operand. It returns True if the left operand is greater, and False otherwise.

# Example:
a = 9
b = 5

# Checking if 'a' is greater than 'b'
print(a > b)  # Output: True

# Checking if 'b' is greater than 'a'
print(b > a)  # Output: False

# Less Than Operator (<) is used to check if the left operand is less than the right operand. It returns True if the left operand is smaller, and False otherwise.

# Example:
a = 9
b = 5

# Checking if 'a' is less than 'b'
print(a < b)  # Output: False

# Checking if 'b' is less than 'a'
print(b < a)  # Output: True

# Less Than or Equal To Operator (<=) is used to check if the left operand is less than or equal to the right operand.
#  It returns True if the left operand is smaller than or equal to the right operand, and False otherwise.
a = 9
b = 5
c = 9

# Checking if 'a' is less than or equal to 'b'
print(a <= b)  # Output: False

# Checking if 'a' is less than or equal to 'c'
print(a <= c)  # Output: True

# Checking if 'b' is less than or equal to 'a'
print(b <= a)  # Output: True

# chaining comparison operators allows you to compare multiple conditions in a single expression, making the code concise and readable. 
# This method checks whether a value satisfies a sequence of conditions without using additional logical operators like and or or.

a = 5

# Chaining comparison operators
print(1 < a < 10)  # Output: True (checks if 'a' is between 1 and 10)
print(10 > a <= 9)  # Output: True (checks if 'a' is less than or equal to 9 and also less than 10)
print(5 != a > 4)   # Output: True (checks if 'a' is not equal to 5 and also greater than 4)



# ---------------------------------------------------------------------Logical Operators---------------------------------------------------------------------


# logical operators are used to combine multiple conditions or boolean expressions. These operators allow you to perform logical operations and control the flow of your program based on multiple conditions. 
# They are essential for decision-making and creating complex conditions.

#example
a = b =c = True , False, True
if a and c:
    print("both a and c are true(AND condtion).")## AND: Both conditions must be True
    if b or c:
        print("either b or c is true(OR condtion).")# OR: At least one condition must be True
        if not b:
            print("b is false (NOT condtion).") # NOT: Reverses the condition

m = 10
n = 8
if m and n:

    m> 8 and n<10

    print("both  m and n are true(OR condition).")
else:
    print("both m and n are false(AND conditon).")


m = 10
n = 8

if m and n:  # Checks if both m and n are non-zero
    if m > 8 and n < 10:  # Additional condition for comparison
        print("Both m and n are true, and the conditions m > 8 and n < 10 are satisfied.")
    else:
        print("Both m and n are true, but the conditions m > 8 and n < 10 are not satisfied.")
else:
    print("Either m or n (or both) are false.")

x =  10
y = 15

if x and y:
    if x >10 or y<10:
        print(" both are satisfied :")
    else:
        print("both are not satisfied:")


#logical AND operator

a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")


    #example-2

    a = 10
b = 12
c = 0
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")

    #python Or operator
    #The Boolean OR operator returns True if either of the operands is True.

    a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")


    #example-2
    a = 10
b = 12
c = 0
if a or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")

    #python NOT operator 

    #Boolean NOT operator works with a single boolean value.
    #If the boolean value is True it returns False and vice-versa.
a = 10

if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
#order of precedence of logical operators
    def order(x):
     print("Method called for value:", x)
     return True if x > 0 else False

a = order
b = order
c = order
if a(-1) or b(5) or c(10):
    print("Atleast one of the number is positive")




# ---------------------------------------------------------------------Question---------------------------------------------------------------------

# Logical Operators in Python - Interview Summary
# Python provides three logical operators to work with boolean values:

# 1. and Operator:

#Returns True only if both operands are True.

#Example:

(5 > 3) and (8 > 5)  # Returns True
#2. or Operator:

#Returns True if at least one operand is True.
#Example:

(5 > 3) or (8 < 5)  # Returns True
#3.not Operator:

#Inverts the boolean value: Returns True if the operand is False, and False if the operand is True.
#Example:
not (5 > 3)  # Returns False


# Difference Between Logical and Bitwise Operators in Python - Interview Summary
# 1.Logical Operators:

# Purpose: Operate on boolean values (True or False).
# Functionality: Used for evaluating logical conditions.
# Examples:

result = True and False  # Logical AND, result is False
result = True or False   # Logical OR, result is True
result = not True        # Logical NOT, result is False
#2.Bitwise Operators:

# Purpose: Operate on integer values at the binary (bit) level.
# Functionality: Perform operations such as AND, OR, XOR, shifts, etc.
# Examples:

result = 5 & 3   # Bitwise AND, result is 1 (0101 & 0011 = 0001)
result = 5 | 3   # Bitwise OR, result is 7 (0101 | 0011 = 0111)
result = 5 ^ 3   # Bitwise XOR, result is 6 (0101 ^ 0011 = 0110)

# Key Difference:

# Logical Operators work on truth values and return boolean results.
# Bitwise Operators work at the binary level and return integer results.

# Logical Operators with Non-Boolean Values in Python - Interview Summary
# Behavior in Non-Boolean Context:

# Python evaluates non-boolean values in a boolean context using logical operators.
# Operator Rules:

# and:
# Returns the first falsy value or the last value if all are truthy.
# Example:

result = [] and "Non-empty"  # Returns []
result = "Hello" and 42      # Returns 42 (both are truthy)
# or:
# Returns the first truthy value or the last value if all are falsy.
# Example:

result = [] or "Non-empty"  # Returns "Non-empty"
result = "" or 0            # Returns 0 (both are falsy)
# not:
# Returns the boolean negation of the value.
# Example:n

result = not []      # Returns True ([] is falsy)
result = not "Hello" # Returns False ("Hello" is truthy)
# Truthy and Falsy Values:

#Falsy: False, None, 0, '', [], {}, set().
# Truthy: All values not considered falsy.

# ---------------------------------------------------------------------Bitwise Operators---------------------------------------------------------------------

# Python Bitwise Operators - Interview Summary

# Python bitwise operators perform operations at the binary level on integers. 
# The integers are converted into their binary representation, and the operations are executed bit by bit. 
# The final result is then returned in decimal format.

# Types of Bitwise Operators

# Operator	  Symbol	          Description	                          Example
# AND	       &	        Performs a bitwise AND operation.	    5 & 3 → 1 (binary: 101 & 011 = 001)
# OR	      `    	`      	Performs a bitwise OR operation.
# XOR	       ^	        Performs a bitwise XOR operation.	    5 ^ 3 → 6 (binary: 101 ^ 011 = 110)
# NOT           ~	        Flips all the bits (1's complement).	~5 → -6 (binary: ~101 = ...1010)
# Left Shift   <<	    Shifts bits to the left, filling with 0.	5 << 1 → 10 (binary: 101 << 1 = 1010)
# Right Shift   >>	    Shifts bits to the right.	5 >> 1 → 2      (binary: 101 >> 1 = 10)

# Key Points
# Decimal to Binary Conversion:

# Operations are performed on the binary representation of numbers.
# Example: 5 → 101, 3 → 011.

# 2.Result in Decimal:

# After bitwise computation, the binary result is converted back to a decimal integer.
# 3.Use Cases:

# Efficient low-level computations.
# Used in algorithms requiring manipulation of binary data (e.g., cryptography, image processing).
# 4.Negative Numbers:

# Represented in two's complement form in Python.
# Examples:

a = 5  # Binary: 101
b = 3  # Binary: 011

print(a & b)  # Output: 1 (AND)
print(a | b)  # Output: 7 (OR)
print(a ^ b)  # Output: 6 (XOR)
print(~a)     # Output: -6 (NOT)
print(a << 1) # Output: 10 (Left Shift)
print(a >> 1) # Output: 2 (Right Shift)

# BitWise AND operator
# Operation: Compares two integers bit by bit.
# Rule: For each bit position, if both corresponding bits in the two integers are 1, the result is 1. Otherwise, the result is 0.

a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)






































































































































































































#--------------------------------------------------------------------Thank you-----------------------------------------------------------------------------










