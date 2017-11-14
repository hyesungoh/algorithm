# 이름 : 오혜성
# 날짜 : 11 14 2017
# 주제 : 별찍기 오른쪽 정렬
n = int(input())
for i in range(1, n+1) :
    print(" "*(n-i), end="")
    print("*"*i)