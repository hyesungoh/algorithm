# 이름 : 오혜성
# 날짜 : 11 29 2017
# 주제 : 시험 성적에 맞는 결과 출력

test = int(input())
print("A" if test >= 90 else "B" if test >= 80 else "C" if test >= 70 else "D" if test >= 60 else "F")
