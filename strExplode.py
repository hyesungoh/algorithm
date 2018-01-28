# 이름 : 오혜성
# 날짜 : 01 24 2018
# 주제 : 문자열 폭발 - 9935

# s = input(); e = input()
# while 1:
#     t = s; s = s.replace(e, "")
#     if t == s: break
# print("FRULA" if s == "" else s)

# 파이썬에서 제일 빠른 Replace, 정규표현식의 sub를 사용해도 시간초과 발생
# from re import sub as sub
# s = input(); e = input()
# while 1:
#     t = s
#     s = sub(e,"",s)
#     if t == s: break
#     # if e in s: s = sub(e, "", s)
#     # else: break
# print("FRULA" if s == "" else s)

# s = list(input()); b = list(input())
# bSize = len(b); b.reverse(); ans = []
# for i in s:
#     ans.append(i)
#     if list(reversed(ans))[0:bSize] == b:
#         for _ in range(bSize): ans.pop()
# print("FRULA" if ans == [] else "".join(ans))

n = list(input()); b = input(); bS = len(b); s = ""
for i in n:
    s += i
    if(s[-bS:] == b):
        s = s[:-bS]
print("FRULA" if not s else s)