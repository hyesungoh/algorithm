# 이름 : 오혜성
# 날짜 : 11 14 2017
# 주제 : 문자열에서 문자 10개 씩 끊어서 출력
s = input(); lS = list(s); n = 0
for i in lS :
    print(i, end=""); n += 1
    if (n == 10) :
        print("\n", end=""); n = 0