# 이름 : 오혜성
# 날짜 : 05 30 2018
# 주제 : 2진수를 8진수로

n = oct(int(input(), 2))
print("".join(list(n)[2:len(n)]))

# print('%o'%int(input(),2))