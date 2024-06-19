#  Shape of array - The shape of an array is number of elements  in each dimensions
# Now we will get the shape iof an array
import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)

#  Now we create 5-D array
import numpy as np
u = np.array([1,2,3,4],ndmin=5)
print(u)
print("The shape of 5-D array: ",u.shape)