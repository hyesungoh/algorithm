# 이름 : 오혜성
# 날짜 : 05 13 2018
# 주제 : 문자열 분석

# ''.isnumeric()
# ''.isupper()
# ''.islower()

while True:
    try:
        l = [0, 0, 0, 0]
        s = input()
        for i in list(s):
            if i.islower():
                l[0] += 1
            elif i.isupper():
                l[1] += 1
            elif i.isnumeric():
                l[2] += 1
            else:
                l[3] += 1
        print(*l)
    except EOFError:
        break
