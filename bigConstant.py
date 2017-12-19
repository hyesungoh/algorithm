# 이름 : 오혜성
# 날짜 : 12 19 2017
# 주제 : 두 수중에 뒤집은 수가 더 큰것 출력

n1, n2 = input().split()
r1, r2 = int(''.join(list(reversed(n1)))), int(''.join(list(reversed(n2))))
print(max(r1, r2))


# 다른 풀이
# print(max(input()[::-1].split()))
