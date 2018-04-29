# 이름 : 오혜성
# 날짜 : 04 29 2018
# 주제 : 별찍기 - 7

n = int(input())
l = list(range(1, n+1)) + list(range(n-1, 0, -1))
for i in l:
    print(" " * (n - i), end="")
    print("*" * ((i * 2) -1))