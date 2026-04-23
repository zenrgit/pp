# [1]. Write a Python code to demonstrate basic operations of list.
#     i. Accessing list elements
#     ii. Adding elements in lists [append ( ), extend ( ), insert( )]
#     iii. Removing elements in lists (remove( ), pop( ) ,clear ( )] 

# Create a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# -------- i. Accessing Elements --------
print("\nAccessing Elements:")
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# -------- ii. Adding Elements --------
print("\nAdding Elements:")

# append()
my_list.append(60)
print("After append(60):", my_list)

# extend()
my_list.extend([70, 80])
print("After extend([70, 80]):", my_list)

# insert()
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# -------- iii. Removing Elements --------
print("\nRemoving Elements:")

# remove()
my_list.remove(25)
print("After remove(25):", my_list)

# pop()
removed = my_list.pop()
print("After pop():", my_list)
print("Popped element:", removed)

# clear()
my_list.clear()
print("After clear():", my_list)