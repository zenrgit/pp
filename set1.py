# [4]. Using Python set operations, create a set named fruits containing "apple", "banana", "mango",
# and "orange". Then add "grape" to the set, remove "banana", and finally discard "mango". 
# What will be the final contents of the fruits set?

# Create set
fruits = {"apple", "banana", "mango", "orange"}
print("Original Set:", fruits)

# Add "grape"
fruits.add("grape")
print("After adding grape:", fruits)

# Remove "banana"
fruits.remove("banana")
print("After removing banana:", fruits)

# Discard "mango"
fruits.discard("mango")
print("After discarding mango:", fruits)