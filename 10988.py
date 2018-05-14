# 이름 : 오혜성
# 날짜 : 05 15 2018
# 주제 : 팰린드롬(회문) 확인

def palin(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-1-i]:
            return 0
    return 1

print(palin(input()))