# Lists have their own methods that can be called. In this section we will go ever the uses of some.
# These methods are exclusive to the list datatype. 
    # .index() | Find where a certain value is within a list
    # .count() | Counts the amount of time a value occurs within a list
    # .append() | Adds an item to the end of a list
    # .insert() | Adds an item to the specified index of a list
    # .remove() | Removes a specified value from a list. Only the first matching instance will be removed. (It is different to using del)
    # .sort() | Sorts a list to be inorder. Do note that Capitals will be sorted first by default.  A-Z a-z
        #    .sort(key=str.lower) | Will sort everything as if it were lower case. 
newList = ["Test", "Test2", "Test3", "Test4", "Test"]
newList.index("Test2") # Returns : 1
newList.count("Test") # Returns : 2

newList.append("Hello") 
print(newList)
newList.insert(1, "Hello2") # Adds "Hello" to the second position / index 1 and shifts the values after to the right (index + 1)
print(newList)

newList.remove("Test4") # Removes "Test4" from the list.
print(newList)

# Sorting Values
numList = [5, 2, 4, 5 ,6, 1]
print(numList)
numList.sort()
print(numList)
    # In reverse
numList.sort(reverse=True)
print(numList)

# It also works for Strings
strList = ["Ted", "Alex", "Jeff", "Dave"]
print(strList)
strList.sort()
print(strList)
strList.sort(reverse=True)
print(strList)