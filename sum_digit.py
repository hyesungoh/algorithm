# 이름 : 오혜성
# 날짜 : 11 23 2017
# 주제 : 자릿수의 합

def sum_digit(num) :
    return sum(list(map(int, list(str(num)))))

print(sum_digit(123))