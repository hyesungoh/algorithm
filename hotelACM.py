# 이름 : 오혜성
# 날짜 : 12 28 2017
# 주제 : 10250번 문제, https://www.acmicpc.net/problem/10250

for i in range(int(input())):
    h, w, n = list(map(int, input().split()))
    hN = round(n/h + .49)
    hH = n - h*(n//h) if n != h*(n//h) else h
    print(hH * 100 + hN)