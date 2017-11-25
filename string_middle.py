# 이름 : 오혜성
# 날짜 : 11 26 2017
# 주제 : 문자열의 가운데 글자 반환

def string_middle(s) :
    return s[len(s)//2] if len(s) % 2 == 1 else s[(len(s)//2)-1 : (len(s)//2)+1]

print(string_middle("power"))
print(string_middle("test"))