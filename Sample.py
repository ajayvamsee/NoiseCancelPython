import numpy as npy

# creating a 2-d array
arr1 = npy.array([1, 3, 5, 7])

# creating a 3-d array
arr2 = npy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# printing the shape of arrays
# first element of tuple gives
# dimension of arrays second
# element of tuple gives number
# of element of each dimension
print(arr1.shape)
#print(arr2.shape)