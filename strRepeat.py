# 이름 : 오혜성
# 날짜 : 12 17 2017
# 주제 : 문자열에서 문자를 반복하여 출력

for i in range(int(input())):
    n, s = input().split()
    print(''.join(list(map(lambda x: int(n) * x, s))))