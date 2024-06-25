# Spliting Array in numpy - it is reverse to joining, breaking the array by using array_split() method.

# Spliting array in 3 parts
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) 

# Now we will split array in 4 parts.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.array_split(arr, 4)
print(newarr)
# Npw we will print trough indexing
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.array_split(arr, 4)
for i in newarr:
  print(i)
  
# Spliting the 2-D array
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
for i in newarr:
  print(i)
  
# Spliting 2-D array into three 2-D arrays.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
for i in newarr:
  print(i)