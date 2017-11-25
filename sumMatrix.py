# 이름 : 오혜성
# 날짜 : 11 26 2016
# 주제 : 행렬의 덧셈

def sumMatrix(a, b) :
    return [[i + j for i, j in zip(I, J)] for I, J in zip(a, b)]

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))