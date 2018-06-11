# 이름 : 오혜성
# 날짜 : 06 11 2018
# 주제 : 2진수 뒤집기

n = bin(int(input()))
rn = list(reversed(list(n)[2:len(n)]))
n = ''.join(rn)
print(int(n, 2))