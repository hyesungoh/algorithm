# 이름 : 오혜성
# 날짜 : 11 21 2017
# 주제 : 띄어쓰기 기준으로 문자열의 첫 문자는 대문자로 표현

def Jaden_Case(s) :
    sList = list(s);
    sList = list(map(lambda x: sList[x].upper() if sList[x-1] == " " else sList[x].lower(), range(len(sList))))
    sList[0] = sList[0].upper()
    return "".join(sList)


print(Jaden_Case("3people unFollowed me for the last week"))