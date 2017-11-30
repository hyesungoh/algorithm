# 이름 : 오혜성
# 날짜 : 11 29 2017
# 주제 : 배열에 들어갈 갯수와 N을 입력 > 배열에 들어갈 수 입력 > n 보다 작은 수 출력

trash, n = input().split()
l = [int(x) for x in input().split()]
for i in list(filter(lambda x: x<int(n), l)):
    print(i, end=" ")