# If we wan't to iterate through a list we can use a FOR loopn
newList = ["x", "y", "z"]
for i in newList:
    print(i)

# If you want to be able to use the index within the loop you should do it this way.
newList = ["x", "y", "z"]
for i in range(len(newList)):
    print(i, "is", newList[i])

# Multiple Assignment
dog = ['Small', "Black", "Timid"]

# If we have a list and we want to assign some variables to the contents we can individually assign them by accessing the index like so
    #size = dog[0]
    #color = dog[1]
    #attitude = dog[2]

# Alternatively, we could do it this way. Python will assign them in order of index starting at [0]
size, color, attitude = dog

# We can also assign values to variables in much the same way
size, color, attitude = "Large", "Grey", "Excited"

# Swapping Variables
# The multiple assignment trick is often used to swap variables
a = "AAA"
b = "BBB"
a, b = b, a # Swaps the values around
print(a)

# Augmented Assignment Operators
# These are just shortcuts that can be helpful.

    # Operator | Equivalent Statement | What
    # += 1 | x = x + 1 | Add to
    # -= 1 | x = x - 1 | Subract
    # *= 1 | x = x * 1 | Multiply
    # /= 1 | x = x / 1 | Divide
    # ?- 1 | x = x % 1 | Modulus(?)