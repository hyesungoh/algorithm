# 이름 : 오혜성
# 날짜 : 12 30 2017
# 주제 : 2775번, a 층의 b 호에 살려면 자신의 아래(a-1)층에 1호부터 b 호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다

for i in range(int(input())):
    k = int(input()); n = int(input());
    l = [list(range(1, n+1))]
    for x in range(1, k):
        l.append([])
        for y in range(n):
            l[x].append(sum(l[x-1][0:y+1]))
    print(sum(l[k-1][0:n+1]))


# 딕셔너리 이용
# dic = {(0,i):i for i in range(1,15)}
# for x in range(1,15):
# 	for y in range(1,15):
# 		dic[(x,y)] = sum([dic[(x-1, k)] for k in range(1,y+1)])
# for _ in range(int(input())):
# 	k, n = int(input()), int(input())
# 	print(dic[(k,n)])

# 팩토리얼 이용
# from math import factorial as fact
# for _ in range(int(input())) :
#     k,n = int(input()),int(input())
#     print(fact(n+k)//(fact(n-1)*fact(k+1)))



