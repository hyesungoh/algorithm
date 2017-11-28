# 이름 : 오혜성
# 날짜 : 11 28 2017
# 주제 : 최대공약수와 최소공배수 반환

def gcdlcm(a, b):
    lcmTemp = a * b; mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return [b, lcmTemp//b]

print(gcdlcm(3, 12))