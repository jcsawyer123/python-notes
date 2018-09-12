# FOR Loops or count controlled iteration
# FOR loops will run for a predetermined number of times
# FOR loops can also use break and continue as covered in 02

# i is a variable, you can pass one in or create a new one. i is typically used as it relates to "index". 
# the range() creates a sequence of values to iterate through (0, 1, 2, 3..)
for i in range(5):
    print(i)
print("==============")

# Range can have 2 values passed into. Value 1 is where it will start, Value 2 is where it will enf
for i in range(5, 10):
    print(i)
print("==============")

# Range can actually have 3 values passed into it. The third value is the STEP argument which states how many it changes each time
# Such as move in 2s
for i in range(0, 10, 2):
    print(i)
print("==============")