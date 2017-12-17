# 이름 : 오혜성
# 날짜 : 12 17 2017
# 주제 : a부터 z까지 처음으로 등장하는 위치 출력, 포함하지 않을 시 -1

s = input()
l = []
for i in range(ord('a'), ord('z')+1):
    try:
        l.append(s.index(chr(i)))
    except:
        l.append(-1)

[print(i, end=" ") for i in l]