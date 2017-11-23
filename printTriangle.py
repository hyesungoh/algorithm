# 이름 : 오혜성
# 날짜 : 11 23 2017
# 주제 : 별찍기 함수

def printTriangle(num) :
    return "".join(["*" * i + "\n" for i in range(1, num+1)])

print(printTriangle(3))