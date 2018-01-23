# 이름 : 오혜성
# 날짜 : 01 24 2018
# 주제 : 문자열 폭발 - 9935

# s = input(); e = input()
# while 1:
#     t = s; s = s.replace(e, "")
#     if t == s: break
# print("FRULA" if s == "" else s)

# 파이썬에서 제일 빠른 Replace, 정규표현식의 sub를 사용해도 시간초과 발생
from re import sub as sub
s = input(); e = input()
while 1:
    t = s
    s = sub(e,"",s)
    if t == s: break
    # if e in s: s = sub(e, "", s)
    # else: break
print("FRULA" if s == "" else s)
