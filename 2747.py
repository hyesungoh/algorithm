# 이름 : 오혜성
# 날짜 : 04 28 2018
# 주제 : 피보나치 함수

def fib(n):
     fibs = [0, 1]
     for i in range(2, n+1):
         fibs.append(fibs[-1] + fibs[-2])
     return fibs[n]

print(fib(int(input())))