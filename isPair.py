# 이름 : 오혜성
# 날짜 : 11 21 2017
# 주제 : 괄호의 쌍이 맞는지 확인

def is_pair(s):
    returnBool = False
    openNum = 0; closeNum = 0
    for i in s :
        if i == "(" :
            openNum += 1
        elif i == ")" :
            closeNum += 1
            returnBool = openNum == closeNum

    return returnBool

print(is_pair("(hello)()"))
print(is_pair(")("))