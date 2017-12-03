# 이름 : 오혜성
# 날짜 : 12 03 2017
# 주제 : 주어진 수 만큼 반복 > 첫 수로 학생의 수, 나머지 수는 점수로 입력 > 한줄 씩 평균을 넘는 학생의 비율 출력

for i in range(int(input())) :
    l = [int(num) for num in input().split()]
    l.remove(l[0])
    over = list(filter(lambda x: x > sum(l)/len(l), l))
    print("%.3f%%" %round(len(over)/len(l) * 100, 4))