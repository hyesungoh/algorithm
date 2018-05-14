# 이름 : 오혜성
# 날짜 : 05 15 2018
# 주제 : 모음의 수

s = input(); n = 0
for i in s:
    if i in 'aeiou':
        n += 1
print(n)