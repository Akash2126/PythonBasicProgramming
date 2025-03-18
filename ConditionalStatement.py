
# If Conditional Statement in Python:
#  if statement is the simplest conditional structure in Python. 
# It executes a block of code only if the specified condition evaluates to True.

age = 20

if age >= 18:
    print("Eligible to vote.")

    # If-Else Conditional Statement in Python:
    # The if-else statement is used to execute a block of code if the condition is True,

    age = int(input ("enter your valid age:"))

    if age >=18:
        print("you are an adult!")
        if age >=60:
            print("you are an seniar citizen!")
    else:
        print("you are an  not adult!")
else:
        print("you are an not a sinear citizen!")

age = int (input("your age:"))
if age>= 18:
  print("you are eligible for loan!")
else:
   print("you are not eligible for the loan!")
print("thankyou for applying!")

#short hand if statement:
# if you have only one statement to execute, you can put it on the same line as the if statement.
age = 25
if age >=18: print("you are eligible to vote!")

#short hand if-else statement:
# if you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
marks = int(input("Enter your marks:"))
res = " Garde A+" if marks >= 80 else "Grade A"
print(f"result:{res}")

#elif statement in Python:
# The elif statement allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

age = int(input("enter your age:"))

if age <= 12:
    print("child.")
elif age <=19:
    print("teenager.")
elif age <=35:
    print("young adult.")
else:
    print("adult.")

#nested if else statement

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

    #ternary conditional statement.
    # Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"

print(s)

#match - case statement 

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

#-------------------------------------------------------------  question/answer------------------------------------------------------------

####Conditional Statements in Python.

# Definition: Allow execution of specific code blocks based on the truth value of a condition.
# Key Constructs:

# .if: Executes code if the condition is true.
# .if-else: Executes one block if the condition is true and another if false.
# .elif: Checks multiple conditions in sequence, executing the first true condition.

# Example:

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
#### Conditional Expressions (Ternary Operator)
# Definition: A concise way to evaluate conditions and assign values based on the result.
# Syntax: value_if_true if condition else value_if_false
# Example:

x = 5
result = "High" if x > 10 else "Low"
print(result)  # Outputs: "Low"
#### Decision-Making Statements
# Purpose: Control program flow based on conditions.
# Types:

# .if: Executes code if the condition is true.
# .if-else: Executes different code blocks based on the condition.
# .elif: Handles multiple conditions.
# .Nested if: Combines conditions for complex logic.

# ###Conditional Selection Statements
# Refer to the use of if, elif, and else to choose specific code blocks to execute based on conditions.

# Conditional Loops

# 1.While Loop:
# Repeats execution while a condition is true.
# Example:

x = 5
while x < 10:
    print(x)
    x += 1
# 2.For Loop:
# Iterates over a sequence.
# Includes conditions with break (exit loop) and continue (skip iteration).
#Example:

for i in range(10):
    if i == 5:
        break
    print(i)



    




         
   