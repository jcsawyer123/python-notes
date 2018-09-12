
# An ':' indicates the start of a block. You can tell if some code is within a block as it will be indented, such as "print('Name Equals Dave')"
# IF and ELIF (ELSE IF) will only execute the contents of their block if their condition returns TRUE
# ELSE will execute the contents of its block if all the previous conditions are all FALSE
#print('Enter a name')

name = input()
if name == 'Dave':
    print('Name equals Dave')
elif name == 'Dave':
    print("what are capitals")
else:
   print("No Dave")

# An if statement can be used to condintionally execute code, depending on whether or not the if statement's condition is TRUE or FALSE.
# An ELIF (An Else If) statement can follow an if statement. It excutes if its condition is TRUE and all previous conditions have been FALSE.
# An ELSE statement comes at the end, it excutes if all other previous conditions have been FALSE.

# -----

# Conditions can use 'Truthy' and 'Falsey' Values
# When using a STRING in a condition a blank string is considered 'Falsey' however, if the string has something within it is 'Truthy'
# The Values 0 and 0.0 are also considered 'Falsey'. 
# When used in conditions they are considered FALSE. You can see yourself which values are Truthy or Falsey by passing them to the bool() function

print('What is your name')
nameTwo = input()
if nameTwo:
    print("Thank You");
else:
    print("name is??????")

# When writing code we should be more explicit. Even though this code works it is not nice code to use.
# Instead the condition should be
  
print('What is your name')
nameTwo = input()
if nameTwo != '':
    print("Thank You");
else:
    print("name is??????")

# This now evaluates if nameTwo is NOT EQUAL (!=) to '' (empty). If it is not empty it runs the condition if it is empty it will return false and print the else block.

