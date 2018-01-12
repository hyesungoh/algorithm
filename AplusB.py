# 이름 : 오혜성
# 날짜 : 01 12 2018
# 주제 : A + B

# 10950
# [print(sum(map(int, input().split()))) for _ in range(int(input()))]

# 10951
# while 1: print(sum(map(int,input().split())))

# 10952
# while 1:
#     l = list(map(int, input().split()))
#     if l != [0, 0]: print(sum(l))

# 10953
# [print(sum(map(int, input().split(',')))) for _ in range(int(input()))]

# 11021
# [print('Case #%s:'%i, sum(map(int,input().split()))) for i in range(1, int(input())+1)]

# 11022
l = []
[l.append(list(map(int ,input().split()))) for i in range(int(input()))]
[print('Case #%s:' %(x+1), y[0],'+', y[1],'=', sum(y)) for x, y in enumerate(l)]