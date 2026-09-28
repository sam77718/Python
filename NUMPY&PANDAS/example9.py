import numpy as np

np.random.seed(90)

A = np.random.randint(1, 20, (3, 3))
B = np.random.randint(1, 20, (3, 3))

print("A:")
print(A)

print("B:")
print(B)


# 1. Element-wise multiplication
C = A * B

print("Multiplication of A & B:")
print(C)


# 2. Actual matrix multiplication
C = np.matmul(A, B)

print("Matrix multiplication:")
print(C)


# 3. Transpose matrix A
A_transpose = A.T

print("Transpose of A:")
print(A_transpose)


# 4. Find determinant of A
A_determinant = np.linalg.det(A)

print("Determinant of A:")
print(A_determinant)


# 5. Find inverse of A
A_inverse = np.linalg.inv(A)

print("Inverse of A:")
print(A_inverse)

#  Verify the inverse

# Multiply A by its inverse:

mul = A * A_inverse
print(mul)