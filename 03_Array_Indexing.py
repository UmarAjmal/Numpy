# 1-D Array Indexing is same as the accessing elementrs of array. 
# start with 0 always.
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

# We can add 3rd and 4th element of list to get new element.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("The result is: ", arr[3] + arr[4])

# Accessing the 2_D Array - Its like rows and columns.
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
print('4th element on 2nd row: ', arr[1, 3])

# Accessing the 3-D - same as accessing
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
print(arr[1, 0, 1])


