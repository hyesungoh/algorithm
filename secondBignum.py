# 이름 : 오혜성
# 날짜 : 11 29 2017
# 주제 : 숫자 세개 입력받은 후 두번째로 큰 수 출력

a,b,c = input().split()
l = [a,b,c]; l = list(map(int, l)); l.remove(max(l)); l.remove(min(l))
print(l[0])

# a,b,c = input().split()
# l = [a,b,c]; l = list(map(int, l)); sorted(l)
# print(l[0])
