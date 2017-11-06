# 이름 : 오혜성
# 날짜 : 11 07 2017
# 주제 : 정수를 리스트형으로 변환 후 뒤집기

def digit_reverse(num) :
    """
    :param num: 정수
    :return: 정수를 리스트형으로 변환 후 뒤집은 리스트
    """
    listNum = list(str(num))

    # str > list 형변환 시 str 식으로 저장되어 다시 정수형으로 형변환
    for i in listNum :
        listNum[listNum.index(i)] = int(i)

    listNum.reverse()
    return listNum

print(digit_reverse(12345))