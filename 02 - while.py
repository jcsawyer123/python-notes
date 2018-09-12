# We can use iteration to run a block of code until a certain condition is met
# Here is a WHILE Loop, it works much like an IF Statement if the condition is TRUE the block of code will be ran. Instead of ending there and going to the next section of code the loop will run again up until the condition is FALSE.

x = 0
while x < 5:
    x = x + 1;
    print (x)

# Here is another example. This loop runs until the user enters something as a name. It is a very simple form of Validation, it just ensures there is SOME data. 
# Note: Validation is not Verification. Validation checks to see if the input conforms with the expected data requirements, such as if inputting a numbere it being within a certain range of values such as 0-255. Verification checks to see if the input is what is intended by the user such as "Your name is (Name), is that correct?"
name = ''
while name == '':
    print('Please enter your name')
    name = input()

# INFINITE LOOPS. You do no want these, if you enter an infinite loop your program will just repeat over and over. If you create one and run it by accident use CTRL+C to exit the program.
# To make sure you can escape a loop when you need within code you can use a BREAK Statement. A break statement will exit out of a loop regardless of if the condition has been met or not.
# In the below example it works the same as the above but this time we could expand the validation to be much more thorough.
nameTwo = '';
while True:
    print('Please enter your name')
    nameTwo = input()
    if nameTwo != '':
        break

# CONTINUE Statement.
# When a continue statement is hit in a WHILE loop it will instantly jump to the next iteration from line 1 of the block instead of executing the current block.
# When this block is ran you will see the iteration for 2 will be missing.
y = 0
while y < 5:
    y = y + 1
    if y == 2:
        continue
    print(y)


