# 이름 : 오혜성
# 날짜 : 03 30 2018
# 주제 : 별찍기 - 5

n = int(input())
for i in range(1, n+1):
    t = i * 2 - 1
    print(" " * (n-i), end="")
    print("*" * t)