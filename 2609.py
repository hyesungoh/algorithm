# 이름 : 오혜성
# 날짜 : 05 25 2018
# 주제 : 최대공약수 최소공배수

def gcd_n_lcm(a, b):
    temp = a * b
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    print(b)
    print(temp//b)


a, b = input().split()
gcd_n_lcm(int(a), int(b))