# 1. Import NumPy
import numpy as np

# 2. Create the arrays
A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

print("Array A :", A)
print("Array B :", B)
print("-" * 30)  #For visual separation

# 3. Basic operations
add      = A + B
subtract = A - B
multiply = A * B
divide   = A / B         

print("A + B :", add)
print("A - B :", subtract)
print("A * B :", multiply)
print("A / B :", divide)
print("-" * 30)

# 4. NumPy functions
mean_A = np.mean(A)
max_A  = np.max(A)
min_A  = np.min(A)
dot    = np.dot(A, B)    

print(f"Mean of A : {mean_A}")
print(f"Max of A  : {max_A}")
print(f"Min of A  : {min_A}")
print(f"Dot product A·B : {dot}")
print("-" * 30)

# 5. Reshape A into a 5×1 column matrix
A_reshaped = A.reshape(5, 1)
print("A reshaped to 5×1:\n", A_reshaped)