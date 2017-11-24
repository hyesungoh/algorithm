# 이름 : 오혜성
# 날짜 : 11 24 2017
# 주제 : x만큼 간격이 있는 n개의 숫자

def number_generator(x, n) :
    return list(range(x, x*n+1, x))

print(number_generator(2,4))