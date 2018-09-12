# In 04 we looked at modules and their functions. Now, we are going to learn how to create our own functions.
# Functions are used when we have a task that we need to do multiple times. 
#   Instead of writing that code again we can use a function to make it easier.

# We define functions using the 'def' keyword.
# funcName = The Functions name it can be anything, keep it related to what it does.
# () = The arguments/parameters we wish to pass to it.
    # def funcName():

# Functions should be defined at the top of the document.


# Workspace
#-------------------------------------------------------------
# Now when we call helloWorld() it will print 'Hello World'
def helloWorld():
    print("Hello World")

helloWorld()
helloWorld()
helloWorld()

#-------------------------------------------------------------

# When we create functions we can also allow them to be passed arguments.
# This is like when we use something such as print(). We pass in arguments for it to be printed.

# When we pass in the argument (Such as 'Dave') which gets assigned to the name parameter
# The name parameter works as a variable within the scope of the function.

# NOTE: Scope will be covered in more detail later.

# Workspace
#-------------------------------------------------------------
def greet(name):
    print("Hey, " + name)

greet('Dave')
greet('Sarah')

#-------------------------------------------------------------

# Sometimes when we call a function we want to return a value.
# To do that we use a return statement.

# NOTE: All functions have a return value. If you do not have a specified return. It will return NONE. (This can sometimes be useful?)

# Workspace
#-------------------------------------------------------------
def addNum(x, y):
    return x + y

outPut = addNum(5, 6);
print(outPut)
#-------------------------------------------------------------
