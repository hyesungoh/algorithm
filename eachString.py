# 이름 : 오혜성
# 날짜 : 12 05 2017
# 주제 : 문자열에서 서로 다른 문자열의 개수

s = input(); l = []
for i in range(0, len(s)):
    for j in range(i, len(s) + 1):
            l.append(s[i:j])

print(len(set(l))-1)
