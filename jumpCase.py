# 이름 : 오혜성
# 날짜 : 11 08 2017
# 주제 : 정수에 1 또는 2를 빼어 나올수 있는 경우의 수 구하기

def jumpCase(num) :
    """
    :param num: 정수
    :return: 피보나치 수열의 자리수
    """
    if (num == 1) :
        return 1
    elif (num == 2) :
        return 2
    return jumpCase(num-1) + jumpCase(num-2)

print(jumpCase(4))