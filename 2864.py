# 이름 : 오혜성
# 날짜 : 05 15 2018
# 주제 : 5와 6의 차이 (경우의 수, 최대최소)

n1, n2 = input().split()
max = int(n1.replace('5', '6')) + int(n2.replace('5', '6'))
min = int(n1.replace('6', '5')) + int(n2.replace('6', '5'))
print(min, max)