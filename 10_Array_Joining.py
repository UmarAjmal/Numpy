# Joining the numpy array - Here we wil pass concatenate.
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1, arr2))
print(arr)

# Joinnig of 2-D array along with row(axis=1).
arr1 = np.array([[1, 2, 3],[4, 5, 6]])
arr2 = np.array([[7, 8, 9],[10, 11, 12]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Joinnig of 2-D array along with stack function.
import numpy as np
arr1 = np.array([[1, 2, 3],[4, 5, 6]])
arr2 = np.array([[7, 8, 9],[10, 11, 12]])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Stacking along with row. using hstack()
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.hstack((arr1, arr2))
print(arr)

#  Stacking along with column. using vstack()
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.vstack((arr1, arr2))
print(arr)

##  Stacking along with height(depth) . using dstack()
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.dstack((arr1, arr2))
print(arr)

