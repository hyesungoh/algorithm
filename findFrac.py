# 이름 : 오혜성
# 날짜 : 11 07 2017
# 주제 : 지그제그 순서로 분수가 들어있는 배열에서 몇번째 분수인지 찾기
#
# 1/1 > 1/2 > 2/1 > 3/1 > 2/2 > 1/3 > 1/4 > 2/4 >
#
# 1/1 1/2 1/3 1/4 1/5
# 2/1 2/2 2/3 2/4
# 3/1 3/2 3/3
# 4/1 4/2
# 5/1
#
def findFrac(num) :
    """
    :param num: 몇번째 분수인지
    :return: 보기쉽게하기 위해 출력을 하였으며 문자열을 리턴
    """
    i = 2
    first = 1
    second = 2
    b = True

    print("1번째 : 1/1")
    if (num == 1) :
        return "1/1"

    while (i <= num) :
        s = str(first)+"/"+str(second)
        print("%s번째 : %s" %(i, s))
        i += 1

        if (first == 1) :
            if (second % 2 == 0) :
                first += 1
                second -= 1
                b = not b
                continue
            else :
                second += 1
                continue

        elif (second == 1) :
            if (first % 2 == 0) :
                first += 1
                continue
            else :
                first -= 1
                second += 1
                b = not b
                continue

        if (b == True) :
            first -= 1
            second += 1
        else :
            first += 1
            second -= 1
    return s


print("정답 : ",findFrac(10))