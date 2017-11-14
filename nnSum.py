# 이름 : 오혜성
# 날짜 : 11 14 2017
# 주제 : n개의 수 공백없이 입력받은 후 합을 출력

num = int(input()); sum = input(); lSum = list(sum); s = 0
for i in lSum :
    s += int(i)
print(s)