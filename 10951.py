# 이름 : 오혜성
# 날짜 : 04 28 2018
# 주제 : python EOF check with a+b-4

while True:
    try:
        print(sum(map(int, input().split())))
    except EOFError:
        break