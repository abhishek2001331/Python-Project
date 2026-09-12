import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# for i in arr:
#     for j in i:
#         print(j, end=" ")
# print()

# #transpose matrix
# for i in np.nditer(arr):
#     print(i , end=" ")
# print()
# mt2 = arr.T
# print(mt2)

# #Sum of all element present in matrix

# print("Sum of arr:", np.sum(arr))
# print("Maximum:", np.max(arr))
# print("Minimum:", np.min(arr))
# matrix1 = np.array([[100,200],[300,400]])
# matrix2 = np.array([[1,2],[3,4]])

# def matrix_product(a, b):
#     return np.dot(a, b)

# result = matrix_product(matrix1, matrix2)

# print(result)

# result = np.dot(matrix1, matrix2)
# print(result)#


#add 2 in every element of matrix1
# matrix1 = matrix1 + 2
# print(matrix1)

# matrix1 = matrix1 - 2
# print(matrix1)

# matrix1 = matrix1 * 2
# print(matrix1)

# arr3 = np.array([[[1,2,10],[3,4,11]],[[5,6,12],[7,8,13]]])
# print(arr3)
# print("Sum of arr3:", np.sum(arr3))
# # print("Maximum:", np.max(arr3))
# # print("Minimum:", np.min(arr3))
# # print("Average:", np.mean(arr3))
# # print("Size:", arr3.size)
# # print("Shape:", arr3.shape)

# print("\nTraversal of arr3:")
# for matrix in arr3:
#     for row in matrix:
#         for element in row:
#             print(element, end=" ")
# print()

a=3
b=5
c= np.bitwise_and(a,b)
print("bitwise_and of a & b is:", c)

c= np.bitwise_or(a,b)
print("bitwise_or of a & b is:", c)

c= np.bitwise_xor(a,b)
print("bitwise_xor of a & b is:", c)

c= np.bitwise_left_shift(a,b)
print("bitwise_left_shift of a & b is:", c)

c= np.bitwise_right_shift(a,b)
print("bitwise_right_shift of a & b is:", c)



