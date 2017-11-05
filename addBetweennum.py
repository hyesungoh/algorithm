# 이름 : 오혜성
# 날짜 : 11 06 2017
# 주제 : 두 수 사이의 정수의 합

def adder(num1, num2) :
    """
    :param num1, num2: 정수
    :return: 매개변수로 온 정수를 포함한 두 정수 사이의 총합 값
    """
    sum = 0

    # 두 수가 같으면 첫 번째 수를 반환
    if (num1 == num2) :
        return num1
    else :
        # 큰 값과 작은 값을 저장하여 연산 수행
        nMax = max(num1, num2)
        nMin = min(num1, num2)
        while (nMin <= nMax) :
            sum += nMin
            nMin += 1

    return sum

print(adder(3, 5))