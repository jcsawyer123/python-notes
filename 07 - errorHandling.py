# When a program crashes, without error handling the whole program will crash. With proper error handling it will continue.
# This has it uses. Do note it won't make a broken program suddenly run and if you have alot of errors they will still need solving.

# Here is an example of an error:

# WORKSPACE
#-------------------------------------------------------------
    # def div(num1, num2):
    #     return num1 / num2

    # print(div(50, 0))
#Result: ZeroDivisionError
#-------------------------------------------------------------

# When an error occurs like this it will crash the program. In cases like this we can resolve it in another way by handling the error.
# We do this using TRY. It works exactly as it sounds it will try to do something first, if it fails it will look to see if it has something else it can do.
# We will be using Try and Except.

# Except is where we can place the error we got and tell the TRY statement what to do if it gets that error instead of crashing.

# WORKSPACE
#-------------------------------------------------------------
def div(num1, num2):
    try: # Trying to do something
        return num1 / num2
    except ZeroDivisionError: # Handling the error
        print("Error: Cannot divide by 0")
        return 0; # If you do not return anyting it will just return NONE. If it was a maths related program it could cause errors late so I set it to 0.

print(div(500, 5))
print(div(50, 0))
#-------------------------------------------------------------

# TRY Statements are used for Validation. That is ensuring a correct/valid input for the program.
# - Another example could be if you take an input and attempt to do something with it and it is the wrong datatype. Instead of crashing you have other options.
# - It would cause a ValueError.

# WORKSPACE
#-------------------------------------------------------------
print("How old are you?")
age = input()
try:
    if int(age) >= 18:
        print('Cool you are an adult')
    else:
        print('No alcohol for you.')
except ValueError:
    print("That is not a number")
#-------------------------------------------------------------

