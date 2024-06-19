import numpy as np
x = np.array([1, 2, 3])
print(x)
print(type(x))
# we can add any list, tuple, or array like object with array() and it will converted into ndarray.
import numpy as np
y = np.array((1, 2.89, "Umar"))
print(y)
print(type(y))

# Dimensions in Array - a dimension in array is one level of array depth (nested array).
# 0-D  array - scalers, are the elements in an array, each value i an array is 0-D array.
# we will create 0-D array with value 42.
import numpy as np
z = np.array(42)
print(z)
print(type(z))

# 1-D Array - An array that has 0-D arrays as its elements is called uni directional or !-D array.
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))
# Create a 2-D array containing 2 arrays with certain values
import numpy as np
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(type(b))

# Now we will create 3-D array with two 2-D arrays.
import numpy as np
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(c)
print(type(c))

# Check how many dimensions an array have : ndim attribute
import numpy as np
a = np.array(42)
b= np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("The dimensions of the arrays are: ",a.ndim)
print("The dimensions of the arrays are: ",b.ndim)
print("The dimensions of the arrays are: ",c.ndim)
print("The dimensions of the arrays are: ",d.ndim)

#  Create an array has 5 dimension and verify that.
import numpy as np
e = np.array([1, 2, 3, 4, 5], ndmin=5)
print(e)
print("The dimensions of the arrays are: ",e.ndim)