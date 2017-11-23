# 이름 : 오혜성
# 날짜 : 11 23 2017
# 주제 : 피보나치 수열

def fibonacci(num) :
    if num == 0 :
        return 0
    elif num == 1 :
        return 1
    else :
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(3))