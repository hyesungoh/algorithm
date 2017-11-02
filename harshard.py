# 이름 : 오혜성
# 날짜 ; 11 02 2017
# 주제 : 하샤드 수 판별

def harshad(num) :
    numStr = str(num)
    numList = list(numStr)
    ciper = 0
    for i in numList :
        ciper += int(i)
    if (num % ciper == 0) :
        return True
    else :
        return False

while (True) :
    insertNum = int(input("정수 입력 : "))
    print(insertNum, "is", harshad(insertNum))