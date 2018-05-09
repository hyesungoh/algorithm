# 이름 : 오혜성
# 날짜 : 05 09 2018
# 주제 : 피보나치 함수

z = [1, 0, 1]
o = [0, 1, 1]

def fivo(n):
    length = len(z)
    if length <= n:
        for i in range(length, n+1):
            z.append(z[i-1]+z[i-2])
            o.append(o[i-1]+o[i-2])
    print(z[n], o[n])

for _ in range(int(input())):
    fivo(int(input()))

# def fivo(n):
#     global n0; global n1;
#     if n == 0:
#         n0 += 1
#         return 0
#     elif n == 1:
#         n1 += 1
#         return 1
#     else:
#         return fivo(n-1) + fivo(n-2)
#
#
# for _ in range(int(input())):
#     n0 = 0; n1 = 0
#     fivo(int(input()))
#     print(n0, n1)