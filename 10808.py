# 이름 : 오혜성
# 날짜 : 04 30 2018
# 주제 : 알파벳 개수

s = input()
for a in range(97, 123):
    print(s.count(chr(a)), end=" ")