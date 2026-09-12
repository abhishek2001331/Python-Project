import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
print("Sum of arr1:", np.sum(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Average:", np.mean(arr1))
print("Size:", arr1.size)
print("Shape:", arr1.shape)

print("\nTraversal of arr1:")
for element in arr1:
    print(element)




arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr2)
print("Sum of arr2:", np.sum(arr2))
print("Maximum:", np.max(arr2))
print("Minimum:", np.min(arr2))
print("Average:", np.mean(arr2))
print("Size:", arr2.size)
print("Shape:", arr2.shape)

print("\nTraversal of arr2:")
for row in arr2:
    for element in row:
        print(element, end=" ")
print()



arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)
print("Sum of arr3:", np.sum(arr3))
print("Maximum:", np.max(arr3))
print("Minimum:", np.min(arr3))
print("Average:", np.mean(arr3))
print("Size:", arr3.size)
print("Shape:", arr3.shape)

print("\nTraversal of arr3:")
for matrix in arr3:
    for row in matrix:
        for element in row:
            print(element, end=" ")
print()

#---------------------------------Full
print(np.full(5,7))
print(np.ones(3))
