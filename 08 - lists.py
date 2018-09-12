# List is a value that contains values.
# It contains multiple values in an ordered sequence.
# Lists start at index 0

# They are denoted by [] with each item seperate by a comma ','
newList = ["One", "Two", "Three"]
# To access a value within a list we use an integer index.
newList[0]
    # = "One"

# It is possible to have lists of lists.
multiList = [["One", "Two", "Three"], [1, 2, 3]]

multiList[0] # Returns the entire first list
multiList[1] # Returns the entire second list

multiList[0][0] # Returns the first item in the first list : "One"
multiList[1][2] # Returns the third item in the second list: 3

# Using negative index
# When we use a negative index it refers to the last index (reverse)
newList[-1] # Returns the last item which is : "Three"
newList[-2] # Returns the second to last item which is : "Two"

# Using a slice
# Sometimes you might want to get a range of values from within a list. 
# Using a slice will return a list of values.
    # When you use a slice it will get the value at the first index but will not get the value at the second.
    # So if you have 0:5 it will get the first value up until but not including the fifth (so it gets the 4th value)
sliceList = ["My", "Name", "Is", "Jeff"]
sliceList[1:3] 

# When using a slice you can leave out a value
#   If you miss out the first index it starts at the beginning
        #sliceList[:3]
#   If you miss out the second index it goes to the end
        #sliceList[2:]

# Changing Values
listX = [1, 2, 3, 4, 5, 6, 7, 8]
print(listX)
listX[5] = listX[5] * 100
print(listX)
listX[0:4] = [100, 200, 300, 400] 
print(listX) 

# Deleting from a list
# To remove from a list we just use the del statement
    # It can be considered an "Unassignment Statement"  
delList = [1, 2, 3, 4, 5]
del delList[1] # Removes the value at the second index which is : 2
print(delList)

# Converting to List
# If we have a string and we want to convert it to a list we can use the list function.
x = list("Hello") # Result : ['H', 'e', 'l', 'l', 'o']
print(x)

# Evaluating if a value IS IN a list
'h' in ['a', 'b', 'c', 'd', 'e'] # Returns : False
'a' in ['a', 'b', 'c', 'd', 'e'] # Retruns : True

# Evaluating if a value IS NOT IN a list
'h' not in ['a', 'b', 'c', 'd', 'e'] # Returns : True
'a' not in ['a', 'b', 'c', 'd', 'e'] # Retruns : False
