# Iteratting Array - means going through the elements one by one or step by step by forloop.

# Iterate 1-D array
import numpy as np

arr = np.array([1, 2, 3])

for i in arr:
    print(i)

# Iterate 2-D array
import numpy as np
aaa = np.array([[1, 2, 3],[4, 5, 6]])
for i in aaa:
    print(i)
    
# Iterte on each Scalar element of 2-D
import numpy as np
aaa = np.array([[1, 2, 3],[4, 5, 6]])
for i in aaa:
    for j in i:
        print(j)
    
# Iterate 3-D array
import numpy as np

aaa = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9],[10, 11, 12]])

for i in aaa:
    for j in i:
        print(j)

#Alternative way:  
# Iterate through nditer() function.
import numpy as np

aaa = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9],[10, 11, 12]])

for i in np.nditer(aaa):
    print(i) 