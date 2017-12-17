# 이름 : 오혜성
# 날짜 : 12 17 2017
# 주제 : 40점 이하인 점수는 40점으로 올림 후 평균 출력

s = 0
for i in range(5):
    n = int(input())
    s += n if n > 40 else 40
print(s//5)

# 다른 사람의 풀이
# print(sum(eval("max(8,int(input())//5),"*5)))