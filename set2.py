# [5]. Given two sets
# set1 = {10, 20, 30, 40, 50} and
# set2 = {30, 40, 50, 60, 70},
# write a Python program to:
#   1. Find the union of set1 and set2
#   2. Find the intersection of set1 and set2
#   3. Find the difference (set1 − set2) 

# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# 1. Union
union_set = set1.union(set2)
print("Union:", union_set)

# 2. Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 3. Difference (set1 - set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)