# 이름 : 오혜성
# 날짜 : 11 26 2017
# 주제 : 문자열 마지막 네글자를 제외하고 *로 바꾸어 반환

def hide_numbers(s) :
    return str('*'*(len(s)-4) + s[len(s)-4:len(s)])

print(hide_numbers("01050361390"))