

#-------------------------------------------------------------input/output--------------------------------------------------------------------------



# print()-print() function. This function allows us to display text, variables and expressions on the console.
print("Hello World!")
#printing variables
#We can use the print() function to print single and multiple variables.
#  We can print multiple variables by separating them with commas
# Single variable
s = "Akash"
print(s)

# Multiple Variables
s = "PRIYA"
age = 25
city = "PATNA"
print(s, age, city)
#output formatting
#Python offers various output formatting techniques like format(), sep and end parameters, f-strings, and % operator for better readability and control.

amount = 150.75
print("Amount: ${:.2f}".format(amount))

#using sep parameter

# end Parameter with '@'
print("Python", end='@')
print("learnwithAkash")

# Seprating with Comma
print('O', 'M', 'G', sep='')

# for formatting a date
print('17', '01', '2025', sep='-')

# another example
print('Akash', 'gmail.com', sep='@')

#using F-string
name = 'Akash'
age = 23
print(f"Hello, My name is {name} and I'M {age} years old")
# using % operator
num = int(input("enter a value:"))

add = num + 15
print("the sum is %d" %add)

#Take multiple input from the user in a single line 

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#taking conditional input from the user 
# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# input()- enables interaction with users by gethering input during program execution

#Python input() function is used to take user input.
#By default, it returns the user input in form of a string. 

name = input("enter your name : ")
print(name)

roses = int(input("How Many Roses??:"))
print(roses)

Roses = float(input("how many roses??:"))
print(Roses)


#find data type of input in python 

a = "Hello World"
b = 10
c = 11.22
d = ("Akash", "Kumar", "Tiwari")
e = ["Learn", "Python", "with"]
f = {"priya": 1, "bharti":2, "patna":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))



#-----------------------------------------------------------------Question--------------------------------------------------------------------------
#Q1. What are Input and Output Files in Python?

# In Python, input files are files from which the program reads data, like text or binary files. 
# Output files are files where the program writes data, such as results, logs, or processed information.

#Q2.What is the Difference Between Input and Output?

# Input is the data a program receives (e.g., user input, files). 
# Output is the data a program produces (e.g., console messages, files).

#Q3. What is Input Process Output in Python?

# Input-Process-Output (IPO) in Python is a programming model:

# Input: Collect data (e.g., user input or files).
# Process: Perform operations or calculations on the data.
# Output: Show results (e.g., print to console or save to a file).

#Q4 How to Write Output in Python?

# Printing to Console:
# Use the print() function to display output in the console.
print("Hello, World!")
# Writing to a File:
# Use file handling to save output to a file.
with open('output.txt', 'w') as file:
    file.write("This is some output data.")
# Using Standard Output Streams:
# Use sys.stdout for more controlled console output.
import sys
sys.stdout.write("This is some output data.\n")









