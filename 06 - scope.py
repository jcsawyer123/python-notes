# SCOPE is something that you need to understand.
# There are GLOBAL and LOCAL Scopes.
# You can think as SCOPES as a container of variables. Each container is seperate and has its own local variables.

# Variables in the GLOBAL Scope is created when the program starts, and are deleted when the program is terminated.
# Variables in the LOCAL Scope are created when the function is called, and are deleted when something is returned (Even if NONE refer to 05)


# 1. Code in a global scope CAN NOT access Local Variables.
# 2. Code in a local scope CAN access global variables
# 3. Code in one functions local scope cannot access variables in a different functions local scope
# 4. The same name can be used in different scopes.

# WORKSPACE
#-------------------------------------------------------------
# Variables defined within a function are said to be part of that function LOCAL Scope.
def example():
    var = "Local to Example" # Local Variable

# Variables defined outside of any functions are said to exist in the GLOBAL Scope
var = "Global" # Global Variable
#-------------------------------------------------------------

# Since Functions can access variables in the Global Scope how do we know which one a function is using? Local or Global?
# It is simple. Python checks to see if there is an 'Assignment Statement' that is a statement declaring a variable within the LOCAL scope of the function.
    # Such as: num = 5;
# If there is none then the variable being accesses is in the GLOBAL scope.

# Assignment Statement = Local Variable
# No Assignment Statement = Global Variable

# If you want to be able to edit a global variable within a function you can use the global statement.
    # global num
# This will tell python that the variable called num is actually referring to the global variable called num

# WORKSPACE
#-------------------------------------------------------------
def exampleTwo():
    num = 66 # Assignment Statement = Local Variable
    print(num)

def exampleThree():
    print(num) 
    
def exampleFour():
    global num
    num = num + 1
    print(num) 

num = 500 # Global Variable

exampleTwo() # Uses Local Variable
exampleThree() # Uses Global Variable
exampleFour() # Uses Global Variable through Global Statement
#-------------------------------------------------------------