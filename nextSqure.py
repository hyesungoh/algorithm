# 이름 : 오혜성
# 날짜 : 11 26 2017
# 주제 : 매개변수가 x의 제곱이라면 x+1의 제곱을 반환, 아닐시 'no' 반환

def nextSqure(num) :
    for i in range(1, num) :
        if i * i == num :
            return (i+1) * (i+1)
    return 'no'

    # from math import sqrt
    # return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2

print(nextSqure(121))