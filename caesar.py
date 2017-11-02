# 이름 : 오혜성
# 날짜 : 11 03 2017
# 주제 : 시저 암호

def caesar(sCode, addChar) :
    """
    :param sCode: 코드화 시킬 문자열
    :param addChar: 각 문자에 더할 수
    :return: 코드화 시킨 문자열
    """
    caesarCode = ""             # 리턴할 변수
    actualAdd = addChar % 25    # 25 이상의 숫자가 넘어왔을 때를 대비
    subAdd = 0                  # z, Z가 넘어갔을 때 추가적으로 더할 값
    nTemp = 0                   # 아스키코드 값을 임시적으로 저장
    listCode = list(sCode)      # 입력받은 문자열을 배열에 저장

    for i in listCode :         # 각 배열의 요소들로 반복 (클로저?)
        # 공백이 아닐 시
        if (i != " ") :
            nTemp = ord(i) + actualAdd  # ord = 아스키코드값을 반환

            # 대문자이고 Z의 아스키코드 값을 넘었을 때
            if (ord(i) <= ord("Z") and nTemp > ord("Z")) :
                subAdd = nTemp - ord("Z") - 1
                nTemp = ord("A") + subAdd

            # 소문자이고 z의 아스키코드 값을 넘었을 때
            elif (ord(i) <= ord("z") and nTemp > ord("z")) :
                subAdd = nTemp - ord("z") - 1
                nTemp = ord("a") + subAdd

        # 공백일 시
        else :
            nTemp = ord(" ")

        # 최종적으로 반환할 문자열 변수에 정수형을 문자로 반환하는 chr()을 이용하여 추가
        caesarCode += chr(nTemp)

    return caesarCode

while (True) :
    insertStr = input("Str : ")
    insertNum = int(input("Num : "))
    print("%s is code to %s" %(insertStr, caesar(insertStr, insertNum)))