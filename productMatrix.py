# 이름 : 오혜성
# 날짜 : 11 24 2017
# 주제 : 행렬의 곱셈

import numpy as np
def productMatrix(A, B):
    return (np.matrix(A)*np.matrix(B)).tolist()

# 동일한 자료형을 묶어주는 함수, zip
# def productMatrix(A, B):
#     return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

#     for a_row in a:
#         for b_col in zip(*b) :
#             for A, B in zip(a_row, b_col) :
#                 A * B

a = [[1, 2], [2, 3]]
b = [[3, 4], [5, 6]]
print(productMatrix(a,b))
