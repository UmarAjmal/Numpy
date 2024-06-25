# Searching Array - You can search a certain value in array and return indeexse that get match by using where() methord.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
for i in x:
    print(i)

# Now we will find the indexes where the values are even:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
for i in x:
    print("Values are even at indexes: ",i)

# Now we will find the indexes where the values are odd:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 != 0)
for i in x:
    print("Values are odd at indexes: ",i)

# Searchesorted() - perform binary search in array
# We wil find the index where the value 7 should be inserted.
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print("Value is placed at indexe: ",x)

# Now we will serch from right side
import numpy as np
arr = np.array([6, 7, 8, 9, 10])
x = np.searchsorted(arr, 7, side='right')
print("Value is placed at indexe: ",x)