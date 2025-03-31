import numpy as np

# 1. 10 dan 49 gacha bo'lgan vektor yaratish
vector = np.arange(10, 50)

# 2. 3x3 matritsa (0 dan 8 gacha bo'lgan qiymatlar bilan)
matrix_3x3 = np.arange(9).reshape(3, 3)

# 3. 3x3 birlik matritsa
identity_matrix = np.eye(3)

# 4. 3x3x3 o'lchamli tasodifiy matritsa
tensor_3x3x3 = np.random.random((3, 3, 3))

# 5. 10x10 tasodifiy matritsa va uning min, max qiymatlari
matrix_10x10 = np.random.random((10, 10))
min_val, max_val = matrix_10x10.min(), matrix_10x10.max()

# 6. 30 o'lchamli tasodifiy vektorning o'rtacha qiymati
vector_30 = np.random.random(30)
mean_val = vector_30.mean()

# 7. 5x5 matritsani normallashtirish
matrix_5x5 = np.random.random((5, 5))
norm_matrix = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())

# 8. 5x3 va 3x2 matritsalar ko'paytmasi
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product_5x2 = np.dot(matrix_5x3, matrix_3x2)

# 9. 3x3 matritsalarning skalyar ko'paytmasi
matrix_A = np.random.random((3, 3))
matrix_B = np.random.random((3, 3))
dot_product = np.dot(matrix_A, matrix_B)

# 10. 4x4 matritsaning transponirlash
t_matrix_4x4 = np.random.random((4, 4)).T

# 11. 3x3 matritsaning determinantini hisoblash
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)

# 12. 3x4 va 4x3 matritsalar ko'paytmasi
matrix_A_3x4 = np.random.random((3, 4))
matrix_B_4x3 = np.random.random((4, 3))
matrix_product_3x3 = np.dot(matrix_A_3x4, matrix_B_4x3)

# 13. 3x3 matritsa va 3x1 vektorning ko'paytmasi
matrix_3x3_random = np.random.random((3, 3))
vector_3 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3_random, vector_3)

# 14. Chiziqli tenglamalar sistemasini yechish
A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
x_solution = np.linalg.solve(A_system, b_system)

# 15. 5x5 matritsaning qator va ustun bo'yicha yig'indilari
matrix_5x5_sum = np.random.random((5, 5))
row_sums = matrix_5x5_sum.sum(axis=1)
col_sums = matrix_5x5_sum.sum(axis=0)

