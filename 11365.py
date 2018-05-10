# 이름 : 오혜성
# 날짜 : 05 11 2018
# 주제 : 암호 해독, 문자열 뒤집기

l = []
while True:
    s = input()
    if s != "END":
        l.append(s)
    else:
        break
[print(''.join(list(reversed(i)))) for i in l]
