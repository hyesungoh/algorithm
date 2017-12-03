# 이름 : 오혜성
# 날짜 : 12 03 2017
# 주제 : 백준 온라인 저지 1110번, 더하기 사이클

c = 0; n = int(input()); s = 0;
if n < 10: n *= 10;
stN = n
while (1):
    c += 1; s = (n%10) * 10 + int(str(sum([int(i) for i in str(n)]))[-1])
    if (stN == s):
        print(c)
        break
    n = s

