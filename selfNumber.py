# 이름 : 오혜성
# 날짜 : 12 10 2017
# 주제 : 10000 이하의 셀프 넘버 출력

def selfCheck(num):
    return num + sum([int(i) for i in str(num)])

numberList = [i for i in range(1, 10001)]
selfedList = []
for i in numberList:
    selfedList.append(selfCheck(i))

for i in sorted(list(set(numberList) - set(selfedList))):
    print(i)