# 이름 : 오혜성
# 날짜 : 11 04 2017
# 주제 : 숫자만큼 단어의 글자 출력

def water_melon(num, word) :
    """
    :param num: 출력할 글자의 수
    :param word: 글자의 수의 기반이 될 단어
    :return: none
    """
    # word에 num을 곱한 후 슬라이싱
    return (word * num)[0:num]

print(water_melon(10, "가나다라"))
print(water_melon(7, "수박"))
