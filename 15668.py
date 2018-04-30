# 이름 : 오혜성
# 날짜 : 04 30 2018
# 주제 : 방 번호

# 시간 계선 필요

def dup(l):
    temp = list()
    for w in l:
        if w in temp:
            return False
        temp.append(w)
    return True

n = int(input())
n1, n2 = n - 1, 1
while True:
    if n1 < n / 2 - 1 or n1 == 0:
        print(-1)
        break
    if dup(list(str(n1) + str(n2))):
        print(n1, "+",n2)
        break
    n1, n2 = n1 - 1, n2 + 1

