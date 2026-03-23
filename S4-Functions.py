# Functions 

# Syntax for function: 
def function_name(parameters):
    """ Doc String """
    # function body 
    # return expression

# function defination:
def even_or_odd(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

# function call:
even_or_odd(24)

# function with multiple parametrs
def add(a,b):
    c=a+b
    return c

result = add(2,4)
print(result)

# Default Parameters
def greet(name = "Guest"):
    print(f"Hello {name}. Welcome !!")

greet()
greet("Niharika Basam")

# Variable Length Arguments:
# Positional and keyword Arguments

# Positional Arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,"niha")

def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_details(name = "Niharika", age = 16, city = " Hyderabad")

# return multiple parameters/statements
def multiply(a,b):
    return a*b,a
result = multiply(5,8)
print(result)

# lambda functions - It is an anonymous function with returning one expression

# syntax for lambda function:
# lambda arguments: expression
# e.g
addition = lambda x,y : x+y
print(addition(5,8))

# map() function - applies a function for all items in a list 
def square(x):
    return x*x
nums = [7,8,9]
result = list(map(square,nums))
print(result)

# lambda function with map 
numbers = [1,2,3,4,5,6]
squared_numbers = list(map(lambda x:x**2,numbers))
print(squared_numbers)

numbers1 = [1,2,3]
numbers2 = [4,5,6]
added_numbers = list(map(lambda x,y:x+y, numbers1,numbers2))
print(added_numbers)

# example 
words = ['banana', 'apple', 'pineapple']
capitalize = list(map(str.upper, words))

print(capitalize)

# map with dictionaries 
def get_name(person):
    return person['name']

persons = [
    {'name': 'krish', 'age':32},
    {'name': 'Jack', 'age': 33}
]

get_names = list(map(get_name, persons))
print(get_names)

# filter() method
def even(num):
    if num%2==0:
        return True
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
filter_even_numbers = list(filter(even,nums))
print(filter_even_numbers)

# lambda function with filter() method 
greater_than_five = list(filter(lambda x:x>5, nums))
print(greater_than_five)

# lambda function with dictionaries
def age_greater_than_25(person):
    return person['age']>32

people = list(filter(age_greater_than_25,persons))
print(people)
