# 이름 : 오혜성
# 날짜 : 11 23 2017
# 주제 : 문자열의 길이가 4, 6인지 숫자로만 이루어져있는지 반환

# isnumeric()과 isdigit()의 차이는 무엇일까?
def alpha_string46(s) :
    return (len(s) == 4 or len(s) == 6) and s.isnumeric()

print(alpha_string46("a234"))
print(alpha_string46("1234"))

