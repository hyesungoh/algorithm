# 이름 : 오혜성
# 날짜 : 12 25 2017
# 주제 : 그룹 단어 체크

m = 0; n = int(input())
for i in range(n):
    l = []
    for j in input():
        if j not in l:
            l.append(j)
        elif l[len(l)-1] != j:
            m+=1
            break
print(n-m)