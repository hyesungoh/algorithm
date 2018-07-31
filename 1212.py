# 이름 : 오혜성
# 날짜 : 07 31 2018
# 주제 : 8진수를 2진수로 변환

# def deleteTwo(n):
#     ln = list(n)
#     return str(''.join(ln[2:]))
#
# n = '0o' + input()
# print(deleteTwo(bin(int(n, 8))))


print(bin(int(input(),8))[2:])