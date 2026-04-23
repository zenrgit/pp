# [6]Given the dictionary my_dict = {'name': 'Rajesh', 'age': 35, 'city': 'Mumbai'},
#  Write a Python program to perform the following operations:
#     1) Add a new key-value pair 'profession': 'Doctor' to the dictionary and display the updated dictionary.
#     2) Modify the value of the key 'age' to 40 and display the updated dictionary.
#     3) Access and print the value associated with the key 'city'. 
#  After performing the above operations, use the updated dictionary to:
#     4) Remove the key-value pair with key 'profession'.
#     5) Print all key-value pairs present in the dictionary.

# Given dictionary
my_dict = {'name': 'Rajesh', 'age': 35, 'city': 'Mumbai'}
print("Original Dictionary:", my_dict)

# 1) Add new key-value pair
my_dict['profession'] = 'Doctor'
print("\nAfter adding profession:", my_dict)

# 2) Modify value of 'age'
my_dict['age'] = 40
print("After modifying age:", my_dict)

# 3) Access value of 'city'
print("City:", my_dict['city'])

# 4) Remove key 'profession'
my_dict.pop('profession')
print("\nAfter removing profession:", my_dict)

# 5) Print all key-value pairs
print("\nAll key-value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)