# Datatypes in python - integer, string, float, boolean, complex.
# Datatyes in numpy: 
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V for fixed chunk of memory for other type ( void )

# Cheaking datatypes of numpy array with d-type
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Cheaking string datatype of numpy array with d-type
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Create an array with define datatype
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Now we will reate an array with data type 4 bytes.
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Converting datatype from exixting array - astype()
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# Converting datatype from integer to boolean
import numpy as np
arr1 = np.array([0, 1, 3])
newarr1 = arr.astype(bool)
print(newarr1)
print(newarr1.dtype)

