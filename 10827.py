# 이름 : 오혜성
# 날짜 : 05 17 2018
# 주제 : 제곱 구하기

# l = input().split()
# l[0] = float(l[0])
# l[1] = int(l[1])
# print("%%" %pow(l[0], l[1]))

# todo : decimal?
import decimal
decimal.getcontext().prec = 10000
n1, n2 = input().split()
print("{0:f}".format(decimal.Decimal(n1)**int(n2)))
