# 이름 : 오혜성
# 날짜 : 12 30 2017
# 주제 : 수 정렬하기

l = []
[l.append(int(input())) for i in range(int(input()))]
[print(j) for j in sorted(l)]

# map 함수의 기능부분을 print로 이용
# [*map(print,sorted(eval('int(input()),'*int(input()))))]