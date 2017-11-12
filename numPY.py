# 이름 : 오혜성
# 날짜 : 11 12 2017
# 주제 : 문자열의 문자의 갯수 비교

def numPY(s) :
    return s.lower().count('p') == s.lower().count('y')

print(numPY('pPooyY'))
print(numPY('abcd'))
print(numPY('pYy'))