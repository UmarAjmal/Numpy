# Reshapping - Means changing shape of array after adding or removing elements.

# Reshapping from 1-D to 2-D array
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.shape)
b = a.reshape(4,3)
print(b)
print(b.shape)

# Reshapping from 1-D to 3-D array
c = a.reshape(2,3,2)
print(c)
print(c.shape)

# Return copy and view concept
# If it give same array in output then it is view
# If it give reshape array in output then it is copy
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(b)
print(b.reshape(4,3).base)

# Unknown Dimesion - You are only allow to one unknown dimension.
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(b)
print(b.reshape(4,3,-1))

# Flattering the array of multidimesional to 1-D array
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.flatten())

