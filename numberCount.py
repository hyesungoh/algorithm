# 이름 : 오혜성
# 날짜 : 12 13 2017
# 주제 : 세 개의 숫자를 곱한 후 0부터 9까지 숫자의 개수 출력

triple = str(int(input()) * int(input()) * int(input()))
[print(triple.count(str(i))) for i in range(10)]