# 이름 : 오혜성
# 날짜 : 11 07 2017
# 주제 : 2진수로 나타냈을 때 1의 개수가 같으면서 다음으로 큰 수

def nextBignumber(num) :
    """
    :param num: 정수
    :return: 매개변수를 2진수로 나타냈을 때 1의 개수가 같으며 다음으로 큰 수
    """
    # 매개변수의 1의 개수를 저장하고 반복문을 돌아 확인
    countOne = list(bin(num)).count('1')
    while (True) :
        num += 1
        if (list(bin(num)).count('1') == countOne) :
            return num

print(nextBignumber(78))