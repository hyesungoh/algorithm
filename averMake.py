# 이름 : 오혜성
# 날짜 : 11 29 2017
# 주제 : 시험 성적 입력 후 점수/최대값 * 100 한 점수들의 평균

n = int(input()); l = [int(i) for i in input().split()]
aver = (sum(list(map(lambda x: (x/max(l)) * 100, l))) / n)
print("%.2f" %round(aver, 2))