
# # def calc_sum (a,b):
# #     sum = a+b
# #     print("sum of a and b is :",sum)
# #     return sum


# # calc_sum(10,20)

# # calc_sum(20,30)

# # calc_sum(30,40)


# # # Example:2
# # #function defination
# # def calc_sum(a , b):#parameters
# #     return a + b

# # sum = calc_sum(5058 , 8580)#function call; arguments
# # print("sum of a and b is :",sum)


# # Example:3

# def print_hello():
#     print("hello")

# # print_hello()
# # print_hello()  
# # print_hello()  
# output = print_hello()  
# print(output)  # None

# # Example:4
# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(10, 20, 30)

# # Example:5
# #function built-in function
# print("Hello", "World", sep=" ", end="!\n")

# # Example:6
# len("Hello")
# type(10)
# range(5)

# #user defined function
# def calc_sum(a, b):
#     return a + b

# #defualt par0 Suggestionsameter
# def cal_prod(a = 5 ,b = 10):
#     print(a*b)
#     return a*b
# cal_prod()

# #WAF to print the legth of a list. (list is the parameter)

# cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
# heroes = ["Ironman", "Thor", "Hulk", "Captain America", "Black Widow"]

# def print_length(lst):
#     print(len(lst))

# print_length(cities)
# print_length(heroes)

# #WAF to print the elements of a list in a single line. (list is the parameter)

# print(heroes[0], heroes[1], heroes[2], heroes[3], heroes[4])

# print(heroes[0], end = " ")
# print(heroes[1], end = " ")

# def print_len(list):
#     for item in list:
#         print(item, end = " ")

# WAF to find the factorial of n. (n is the parameter)

# def cal_fact(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact *= i
#         print(fact)

#         cal_fact(6)

#waf to convert usd to inr

def converter(usd_val):
    inr_val = usd_val * 83  # 1 USD = 83 INR
    
    print(usd_val, "USD =", inr_val, "INR")  # Correct indentation

converter(73)

#python function with parameters

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

 



