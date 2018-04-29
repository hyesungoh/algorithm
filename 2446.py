# 이름 : 오혜성
# 날짜 : 04 29 2018
# 주제 : 별찍기 - 9

n = int(input())
l = list(range(n, 0, -1)) + list(range(2, n+1))
for i in l:
    print(" " * (n - i), end="")
    print("*" * ((i * 2) -1))