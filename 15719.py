# 이름 : 오혜성
# 날짜 : 05 17 2018
# 주제 : 중복된 수

# todo : 메모리 추가 오류 고치기

n = input()
l = input().split()
li = []

for i in l:
    if i not in li:
        li.append(i)
    else:
        print(i)
        break