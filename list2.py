# [2]. Write a Python code to demonstrate basic operations of list.
#     i. Modifying elements in lists [by index, by slicing]
#     ii. List methods [sort( ),reverse(),index( ),count( ),copy( )]

# Create a list
my_list = [50, 20, 40, 20, 10]
print("Original List:", my_list)

# -------- i. Modifying Elements --------
print("\nModifying Elements:")

# By index
my_list[1] = 25
print("After modifying index 1:", my_list)

# By slicing
my_list[2:4] = [60, 70]
print("After modifying by slicing:", my_list)

# -------- ii. List Methods --------
print("\nList Methods:")

# sort()
my_list.sort()
print("After sort():", my_list)

# reverse()
my_list.reverse()
print("After reverse():", my_list)

# index()
print("Index of element 25:", my_list.index(25))

# count()
print("Count of element 20:", my_list.count(20))

# copy()
new_list = my_list.copy()
print("Copied List:", new_list)