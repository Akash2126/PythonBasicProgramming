

#----------------------------------------Vriables------------------------------------------------

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive (myVar and myvar are different).
# Avoid using Python keywords (e.g., if, else, for) as variable names.

#Variables act as placeholders for data.
#They allow us to store and reuse values in our program.

# variable X stores the integer value 10
# variable name stores a string "Akash"

#example

age= 22

_name = "Akash"

Total_Score = 90

#assigment 
x = 10
y = 15
z = 20

#Danamic Assignment

#python variables are dynamically typed, so the same variable can hold different types of values during excution

x = 10
x = "now a string"

#multiple Assingments
#python allow multiple varibles to be assigned values in a single line.

#python allows assigning the same value to multiple varibles in a single line,
#which can be useful for intializing varibles with the same name.

a = b = c = 100
print(a, b, c )

#assign diff. value to multiple variables simultaneously
x, y, z = 1, 2.5, "python"
print(x, y, z)

#Basic Casting Functions
#  int() - converts compatible values to an integer.
# float() -Transform values into floating- point numbers.
# str()- converts any data type into a string
 
 # Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
abc = 5
f = float(abc)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(abc)  
print(s2)

#Getting the type of Varibles 
#determine the type of varible using type()
# this built-in function returns the type of object passed to it

# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

#scope of varibles - two methods to define scope of varible in py.
# (1) local varible- Variables defined inside a function are local to that function
def f():
    a = "its a local"
    print(a)
    
    f()

# (2)Global VVarible- varibles defined outside any function are global and can be accessed inside function using global keyword
a = "I am global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)

#delete varible using "del" keyword
#remove a variable from the namespace using the del keyword

# Assigning value to variable
x = 10
print(x) 

del x

#Practical examples 
#Swapping two varibles 
#we can swap the value wihtout any temp variable

a, b =5, 10
a, b = b, a 
print(a, b)

#counting characters in a sting
word = "python"
length = len(word)
print("length of the word:", length)

#----------------------------------Questions--------------------------------------------------

# 1. what is the scope of varible in python
# A variable's scope defines where it can be used: 
# local variables are limited to their function, while global variables are accessible everywhere.

# 2.Can we change the type of a variable after assigning it?
# Yes, Python allows dynamic typing. 
# A variable can hold a value of one type initially and be reassigned a value of a different type later.

# 3. What happens if we use an undefined variable?
# Using an undefined variable raises a NameError. Always initialize variables before use.

# 4.How can we delete a variable in Python?
# We can delete a variable in Python using the del keyword:







