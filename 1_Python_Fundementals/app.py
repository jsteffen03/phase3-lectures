#!/usr/bin/env python3
import ipdb
import math
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py

#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
# print("Hello World!")

#Python Package Index
#To install packages use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 
#What is pipenv shell?

#Debugging using ipdb
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
# ipdb.set_trace()

# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements

#Variables
#Todo 5: Create a variable and assign it to a value
test = 10
# print(test)

x = "Fish"
# print(x)

#Python Data Types
#Todo 6: Create a data type variable

#str
string = 'STRING'

#int
integer = 10

#float
float_var = 10.5

#bool
booleanT = True
booleanF = False

#None
undefined = None

#list
# notArrayButList = []
not_array_but_list = ["apple","orange","grape","grape","apple","apple"]
# print(not_array_but_list[1])
not_array_but_list.append("watermelon")
# print(not_array_but_list)

#Tuple
tup = ("apple",)
# print(tup[0])
# tup.append("waterwelon")

#Set
# set_var = {"apple","orange","grape","grape","apple","apple"}
# set_var.add("watermelon")
# print(set_var)
list_to_set = set(not_array_but_list)
# print(list_to_set)
x = 0 
# print(bool([1]))
# print(set(string))
int_maybe = "20"
# print(int(int_maybe))
#Dictionary
# print(dict(not_array_but_list))
dictionary = {
    "key": "value",
    "test": 0
}
# print(dictionary["test"])
# print(dictionary.get("key","Default"))
dictionary["key2"] = "Test"
# print(dictionary)

#Type Conversion
#Todo 7: Perform type conversion on a data type

#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true
if True:
    print("In true")
    print("tabbed over")
else:
    pass
print("hi")
# print("Yell")
#if/else syntax
#if condition:
#else:


#if/elif/else syntax
x = "panda"
if x == "red":
    print("Color")
elif x == "panda":
    print("Animal")
else:
    print("Other")
#if condition:
#elif:
#elif:
#else:

#Syntax of a ternary
#[option1] if [condition] else [option2]
# statement ? true: false
# [condition] ? [option1] : [option2]
print("true terniary") if x == "panda" else print("false terniary")

#Comparison Operators:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# is
list1=["test","test2"]
testlist = list1
list2=["test","test2"]
print(type(list1))
if list1 is list2:
    print("Using is")
else:
    print("This is false")

#Logical Operators
#and, or, not
# && || !
list = ["test"]
if len(list) > 0 and list[0] == "test":
    print("In this and statement")

#While Loop
#For Loop and Range
fruits = ["apple","orange","grape","grape","apple","apple"]
for x in fruits:
    # `${x}`
    print(f"The current fruit is {x}, lets eat it")

countdown = 10
while countdown >= 0:
    print(f"COUNTDOWN {countdown}")
    countdown -= 1

def AddTwo(x,y):
    # print(x+y)
    if True:
        pass
    return x+y

added = AddTwo(5,6)
print(added)
# AddTwo = "Overwritten"

#Conditionals and Control Flow

#Test if a number is positive
number = 1
if number > 0:
    print("Positive!")

#Test if a string is empty
string = ""
if not string:
    print("String is empty")

#Test if a number is positive or negative using an else
#Test if a number is positve, negative, or zero, using if, elif, and else
number = -19
if number > 0:
    print("Positive!")
elif number == 0:
    print(0)
else:
    print("Negative")


#Test if a number is in between two numbers using the and operator
if 0 < number < 20:
    print("Between")

#Test if a number is positive, even, or both
if number > 0 or number%2 == 0:
    print("Good")

#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternary


#String Interpolation example
#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"

#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

#Todo 11: Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

#Todo 12: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

