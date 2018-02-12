# 이름 : 오혜성
# 날짜 : 02 13 2018
# 주제 : 패턴 체크, 9996번

n = int(input())
p = input().split('*')
for _ in range(n):
    s = input()
    ans = False
    if s.startswith(p[0]):
        s = s.replace(p[0], "")
        if s.endswith(p[1]):
            ans = True
    print("DA" if ans else "NE")