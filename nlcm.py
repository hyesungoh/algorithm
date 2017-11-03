# 이름 : 오혜성
# 날짜 : 11 04 2017
# 주제 : n개의 숫자의 최소공배수

def lcm(num1, num2) :
    """
    :param num1, num2: 두개의 수를 받음
    :return: 두 수의 최소공배수
    """
    returnNum = max(num1, num2) # 두 수중 큰 값을 저장
    # 두 수중 큰 값부터 두 수를 곱한 값까지 반복
    for i in range(returnNum, num1 * num2 + 1) :
        # 증가하는 값이 매개변수로 받은 두 수와 나누어질 때
        if (i % num1 == 0 and i % num2 == 0) :
            return i

def nLcm(numsList) :
    """
    :param numsList: 정수가 담겨있는 배열
    :return: 배열이 담고있는 수들의 최소공배수
    """
    loL = len(numsList)         # length of List
    for i in range(1, loL) :
        # 각 수들의 최소공배수를 구하여 저장
        numsList[i] = lcm(numsList[i], numsList[i-1])

    return numsList[loL - 1]

test = [2, 6, 8, 14]
print(nLcm(test))