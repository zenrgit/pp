import numpy as np

# -------- 1D Array --------
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# -------- 2D Array --------
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# -------- Reshaping --------
reshaped = arr1.reshape(5, 1)
print("\nReshaped 1D to 2D:\n", reshaped)

# -------- Indexing --------
print("\nFirst element of 1D array:", arr1[0])
print("Element at row 1, column 2 in 2D array:", arr2[1][2])

# -------- Slicing --------
print("\nSlicing 1D array (index 1 to 3):", arr1[1:4])
print("Slicing 2D array (first row):", arr2[0, :])
print("Slicing 2D array (second column):", arr2[:, 1])