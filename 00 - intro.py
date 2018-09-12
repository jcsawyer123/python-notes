# This document covers alot of things.
# It is expected that you will already know the basics:
# - What a varaible is
# - What DataTypes are
# - Getting user input
# - Printing
# - And etc

# This document should be used to remind you of syntax of these basics while also including some extra information that can be useful



# Declaring Variables
# - In Python you do not have to explicitly state the DataType of a variable as it 'Dynamically Typed'. However it is also "Strongly Typed" so as soon as a variable
#   you must explicitly convert it (Covered later.)
x = 5
name = 'Dave'

# Printing / Outputting Text
#-------------------------------------------------------------
print('Hello')
textVar = 'Hello'
print(textVar)
#-------------------------------------------------------------

# Getting user input
# - Both are valid ways of taking input. I would use the second way though.
#-------------------------------------------------------------
textInput = input("Input?")

print('Input??')
textInputTwo = input()
#-------------------------------------------------------------

# Joining Strings Together (concatenation)
# - If you want to join multiple strings together, including string variables this is how you do it. 
#-------------------------------------------------------------
nameIn = input("What is your name")
print ("Hello " + nameIn + " , nice to meet you.")
#-------------------------------------------------------------
# You can add multiple strings by also just using a , by default it will add a space.
#-------------------------------------------------------------
print("Hello", "my", "name", "is", "Jeff")
# result: Hello my name is Jeff


# 'Advanced Print'
# end='' changes what comes at the end of a string. If you make it blank there is no newline after.
#-------------------------------------------------------------
print("Hello", end="")
print("World")
# result: HelloWorld
#-------------------------------------------------------------
# sep='' changes what the , is sustituted for in this case it is a - instead of a space.
#-------------------------------------------------------------
print("1", "2", "3", sep="-")
#-------------------------------------------------------------


# Converting Type
# - There are inbuilt functions to convert type.
# str(var) - Converts to string
# int(var) - Converts to int
# There are more but you will discover them as needed.
#-------------------------------------------------------------
numInt = 2
print("Your numInt is " + str(numInt))

num = input("Give me a number?")
print(5 * int(num))
#-------------------------------------------------------------
