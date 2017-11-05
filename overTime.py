# 이름 : 오혜성
# 날짜 : 11 06 2017
# 주제 : 수들의 제곱수 계산에서 제일 작은 총합 유추, 야근 지수 줄이기

def noOvertime(num, listWorks) :
    """
    :param num: 배열안의 숫자를 감소할 수 있는 횟수, 할 수 있는 일의 양
    :param listWorks: 정수형 배열, 남아있는 일의 양
    :return: 남아있는 일의 양의 총 제곱수를 최소화한 값
    """
    leastWork = 0

    # 횟수만큼 제일 큰 수에서 -= 1
    while(num > 0)  :
        maxNum = max(listWorks)
        listWorks[listWorks.index(maxNum)] -= 1
        num -= 1

    # 배열의 요소를 제곱하여 +=
    for i in listWorks :
        leastWork += (i*i)

    return leastWork

work = [4, 3, 3]

print(noOvertime(4,work))