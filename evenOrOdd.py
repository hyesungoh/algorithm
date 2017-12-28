# 이름 : 오혜성
# 날짜 : 12 28 2017
# 주제 : 짝수 홀수 판별

def evenOrOdd(n):
    s = 'Even' if n % 2 == 0 else 'Odd'
    # return num % 2 and "Odd" or "Even"
    return s
print(evenOrOdd(2))
print(evenOrOdd(3))
