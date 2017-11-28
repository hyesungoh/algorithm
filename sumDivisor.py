# 이름 : 오혜성
# 날짜 : 11 28 2017
# 주제 : n의 약수의 합

def sumDivisor(num):
    return sum(list(filter(lambda x: num % x == 0, range(num,0,-1))))

print(sumDivisor(12))