# Slicing Array - is taking elements to one gven index to other index.
# [start:end],[start:end;step] symtax of slicing

# Imagine you have a delicious pizza, and you want to grab a slice. Slicing in NumPy is like taking a specific portion of your array, just like taking a slice of pizza.

# Now we will slice an eement to 1 to 5.
import numpy as np
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(g)
print(g[1:5])
print(g[4:8])
# Step: you will use step value to determine the stepof the slicing
print(g[1:6:2])

# Now we slice from index 4 to end value
import numpy as np
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(g)
print(g[4:])

# Now we slice from beginnig to index 4 
import numpy as np
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(g)
print(g[:4])

# Now we slice negitively from index 4 to end value
import numpy as np
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(g)
print(g[:-4])

# Now we slice negitively from beginnig to index 4 
import numpy as np
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(g)
print(g[-4:])

# slicing of 2-D array
import numpy as np
h = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(h)
print(h[0:2, 1:3])