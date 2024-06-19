# Difference between numpy copy & view
# We wil make a copy change in original array and display both
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
x[0] = 42
print(arr)
print(x)

# We wil make a view change in original array and display both
import numpy as np
a = np.array([33, 44, 55, 66, 77])
y = a.view()
y[3] = 42
print(a)
print(y)

 