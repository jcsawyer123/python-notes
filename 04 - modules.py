# All Python programs can call upon Pythons 'Built-in Functions' such as:
# - Input() | Gets user Input
# - Len() | Gets the length of a string or list
# - Print() | Prints a string
# Python also comes with what is known as the 'Standard Library' which is a set of modules.
# Each module is a Python program which contains functions that can be used in your program such as:
# Math | The math module has a bunch of useful math related functions
# Rand | The rand module can generate random values and etc

# To be able to use the 'Standard Library' we need to import the desired modules. We do that with the IMPORT statement.
    # import random
    # import math
# You can import multiple modules at once by seperating them with a comma.
    #import random, math, sys, os
# Another way of importing modules allows you to run the functions found within without having to include 'ModuleName.'
# This imports all (*) the functions of random and allows them to be called directly like 'randint(1, 10)'
    #from random import * 
# It is better to use the full import statement when possible as it creates easier to read code.


# Workspace
#-------------------------------------------------------------
import random, math, sys, os


# To be able to use a function within the module we have to do modulename.function()
# The following code will generate a random integer within the range of 1 - 5 and store it within the variable 'x'
x = random.randint(1, 5)
print(x)

sys.exit() #Immediately quits your program
print("Nooooo!") # Will never be ran due to sys.exit()

#-------------------------------------------------------------
# Find out more about standard library modules here:
    #https://docs.python.org/3/library/
# Maths | https://docs.python.org/3/library/math.html
# Random | https://docs.python.org/3/library/random.html
# Sys | https://docs.python.org/3/library/sys.html

# There are also Third-Party Modules. However, they will likely not be useable in-school. They use the PIP command, feel free to research.