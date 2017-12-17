# 이름 : 오혜성
# 날짜 : 12 17 2017
# 주제 : OX 퀴즈

for i in range(int(input())):
    s = input()
    l = list(map(lambda x: sum(range(len(x), 0, -1)), s.split('X')))
    print(sum(l))
