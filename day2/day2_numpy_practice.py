# day2_numpy_practice.py
import numpy as np
import time
np.random.seed(42)
array_3x4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("3x4 array:")
print(array_3x4)
print("Shape:", array_3x4.shape)
second_row = array_3x4[1]
print("Second row:",second_row)
third_column = array_3x4[:,2]
print("Third column:",third_column)
element = array_3x4[1,2]
print("The element:",element)
numbers = np.arange(12)
print("Original numbers:")
print(numbers)
print("Original shape:",numbers.shape)
reshaped = numbers.reshape(3,4)
print("Reshaped numbers:")
print(reshaped)
print("Reshaped shape:",reshaped.shape)
column_means = np.mean(array_3x4,axis = 0)
print("Column means:",column_means)
row_means = np.mean(array_3x4,axis = 1)
print("Row means:",row_means)
mean_value = np.mean(array_3x4)
std_value = np.std(array_3x4)
standardized = (array_3x4 - mean_value) / std_value # Z-score standardization: mean -> 0, std -> 1
print("Std:", std_value)
print("Standardized array:")
print(standardized)
print("Standardized mean:", np.mean(standardized))
print("Standardized std:", np.std(standardized))
random_numbers = np.random.randn(100)
print("First 10 random numbers:")
print(random_numbers[:10])
print("Random shape:", random_numbers.shape)
print("Random mean:", np.mean(random_numbers))
print("Random std:", np.std(random_numbers))
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
B = np.array([
    [10, 20],
    [30, 40]
])
print("A shape:", A.shape)
print("B shape:", B.shape)
C = A @ B
print("A @ B =")
print(C)
print("C shape:",C.shape)
# The broadcast mechanism of numpy
# In NumPy, dimensions are specified using tuples
# Broadcasting typically occurs only when performing element-wise operations on multiple arrays whose shapes differ.
# Broadcasting compares shapes from right to left.
# Case 1 : The dimensions of the two arrays are identical when compared from the last dimension to the first.
# Case 2 : When some dimensions of the two arrays have unequal sizes, one of the arrays has a size of 1 in that unequal dimension.
# BroadCast Mechanism Practice :
bias = np.array([10,20,30,40])
print("Bias shape:",bias.shape)
broadcast_result = array_3x4 + bias
print("Broadcasting result:")
print(broadcast_result)
start_time = time.time()

python_result = []
for number in range(1000000):
    python_result.append(number * number)

end_time = time.time()
print("Python for loop time:", end_time - start_time)

start_time = time.time()

numbers_np = np.arange(1000000)
numpy_result = numbers_np * numbers_np

end_time = time.time()
print("Numpy vectorized time:",end_time - start_time)
