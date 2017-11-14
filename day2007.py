# 이름 : 오혜성
# 날짜 : 11 14 2017
# 주제 : 2007년 x월 y일의 요일

x, y = input().split()
x = int(x); y = int(y)
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for i in range(1, x) :
    y += month[i - 1]
print(days[y % 7 - 1])
